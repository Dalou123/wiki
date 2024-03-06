# CS50 Wiki
This repository is an application of the [Wiki](https://cs50.harvard.edu/web/2020/projects/1/wiki/) assignment from Harvard's CS50’s Web Programming with Python and JavaScript course.

* It's a Wikipedia-like online encyclopedia where users can view, add, remove and edit existing entries.
* Some sample entries are already added to better illustrate the webapp's functionality.
* Each entry is saved as a `.md` file. So when the user modifies it, the file is updated accordingly.
* When users create an entry, they have the ability to format the text using markdown.
* There is a sidebar on the left that allows user to use the different functionalities available, such as:
  - Searching for an entry
  - Navigating to the homepage
  - Creating a new entry
  - Navigating to a random page

[Here](https://youtu.be/bsbB89S5PZw) is a video demonstration of the project with all the functionalities.

# How to run this project
1. First, make sure you have at least [Python](https://www.python.org/) 3.10 installed

2. Create a virtual environment and install requirements:

   - For Windows
        ```
        py -m venv .env
        .env\Scripts\activate.bat
        pip install -r requirements.txt
        ```
   - For Unix
        ```
        python3 -m venv .env
        source .env/bin/activate
        pip install -r requirements.txt
        ```
3. Make migrations (to generate the database) and run the server
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
4. You should now get a link similar to `http://127.0.0.1:8000` which opens your local host at port 8000.
