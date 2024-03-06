import markdown2
from . import util
from random import choice
import os


def generate_page(title):
    """
    find the requested page and return it as formatted html.

    :return The entry as a markdown object in HTML form
            or None if not found
    """
    # first get the entry as a string in markdown syntax
    entry = util.get_entry(title)

    if entry:
        return markdown2.markdown(entry)

    return entry


def save_entry(title, body):
    """
    save the entry to a file, if entry with same title already exists, it is
    replaced
    """
    with open(f"entries/{title}.md", 'wb') as the_file:
        the_file.write(f"# {title}\n".encode('ascii'))
        the_file.write(body.encode('ascii'))


def get_random_page():
    """
    get a random title from the list of entries
    """
    return choice(util.list_entries())


def list_entries_lowercase():
    """
    get the list of entries all in lowercase
    """
    return [i.lower() for i in util.list_entries()]


def delete_entry(title):
    """
    delete an entry file
    """
    os.remove(f'entries/{title}.md')


def open_entry(title):
    """
    open an entry and return the body as a string
    """
    with open(f'./entries/{title}.md', 'r') as file:
        contents = file.read().split("\n", maxsplit=1)
        body = contents[1]

    return body
