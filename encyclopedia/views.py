from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

from . import util
from . import functions


class CreateEntryForm(forms.Form):
    page_title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)


def index(request):
    """
    main page, displays a list of all available entries
    """

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()})


def display_entry(request, title):
    """
    display a page containing the entry requested
    """

    # generate the page as HTML or None if entry not found
    my_page = functions.generate_page(title)

    if my_page:
        return render(request, "encyclopedia/entry.html",
                      {"name": title, "entry": my_page})

    else:
        return render(request, "encyclopedia/error.html", {"name": title})


def random_page(request):
    """
    choose a random page, then redirect the user to this page
    """
    return redirect("wiki:title", title=functions.get_random_page())


def search(request):
    """
    get the search query from the user then:
    redirect the user to the page requested if there is only one result
    render the results list if there is more than one result or no results
    """
    # get the search query in lowercase
    query = request.GET.get("q").lower()

    # get the list of entries in lowercase
    all_pages = functions.list_entries_lowercase()

    # find an exact match
    results = [i for i in all_pages if query == i]

    if len(results) == 1:
        # if there is an exact match, redirect to that result
        return redirect("wiki:title", title=results[0])

    else:
        # if there's no exact match, find all substring matches and display them
        results = [i for i in all_pages if query in i]
        variables = {"query": query, "results": results}

        if len(results) > 0:
            variables["no_exact_match"] = "No exact match found, here are the" \
                                          f" results containing '{query}':"

        return render(request, "encyclopedia/search_results.html", variables)


def create(request):
    """
    Generate a form that allows the user to create a new page and process the
    form when the button is clicked
    """

    if request.method == "POST":
        # create a new form instance containing the contents of the POST request
        form = CreateEntryForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["page_title"].title()
            body = form.cleaned_data["body"]

            if title.lower() not in functions.list_entries_lowercase():
                # if the title is new, add entry into the entries folder
                functions.save_entry(title, body)

                # redirect user to the new entry page
                return HttpResponseRedirect(reverse("wiki:title",
                                                    kwargs={'title': title}))

            else:
                # if title already exists, return the form with an error message
                return render(request,
                              "encyclopedia/create.html",
                              {'form': form, "error": "Title already exists!"})

        else:
            # if the form is not valid, return the form with an error message
            return render(request, "encyclopedia/create.html", {'form': form,
                                                                "error": None})

    else:
        return render(request,
                      "encyclopedia/create.html",
                      {'form': CreateEntryForm(), "error": None})


def edit(request, title):
    """
    Generate a form filled with the existing data in order to edit an entry
    user can delete the form, cancel the changes, save the changes
    """
    if request.method == "POST":
        form = CreateEntryForm(request.POST)

        if "delete" in request.POST:
            functions.delete_entry(title)

            # return to the main page
            return HttpResponseRedirect(reverse("wiki:index"))

        elif form.is_valid():
            # save changes and return to the edited entry
            new_title = form.cleaned_data["page_title"].title()
            body = form.cleaned_data["body"]

            # delete original entry (in case the filename was changed)
            functions.delete_entry(title)

            # save the entry in a new file
            functions.save_entry(new_title, body)

            # redirect user to the edited entry
            return HttpResponseRedirect(reverse("wiki:title",
                                                kwargs={'title': new_title}))

        else:
            # if form is invalid, return with an error message
            return render(request, "encyclopedia/edit.html", {"form": form})

    else:
        body = functions.open_entry(title)
        form = CreateEntryForm(initial={"page_title": title, "body": body})

        return render(request,
                      "encyclopedia/edit.html",
                      {"original_title": title, "form": form})
