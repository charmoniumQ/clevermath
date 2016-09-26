Clevermath
-----------

This project is a Django project with a SQLite backend for development purposes. When the code is deployed in production, it will be a `mod-wsgi` application with a mysql backend.

- Before running any commands, run `. bin/activate` to enter the virtual environment.
- This will activate the copy of `python3.4` included in this project.
- It will activate `django 1.10.1`
- It will put `(clevermath)` in front of your prompt to remind you that you are inside this project's virtual environment
- Run `deactivate` to return to your normal system.

So far, there is one django project called `clevermath` and the following django apps:

- `problem_writer`: for creating problems, editing them, and responding to user flags
- `user_management`: for changing passwords, user email, and other settings
- `problems`: for users to read and answer problems
- `stats`: for useres to get statistical reports

These divisions are not set in stone, and we can change them if something else makes more sense.
