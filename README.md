# Flask Restful New Project Structure

>This repository is structure to start a new flask restful project. Contains enter and mid level project.

>**This structure is not done!**

### If you want to use this structure. Pay attention to the items below!

- You need Git VCS [Download](https://git-scm.com/downloads)
- You need Python3.0 or newer version.[Download](https://www.python.org/downloads/)
- You need pip package manager for python. If you have python, you already have pip.
- Absolutely you need virtualenv. [Virtual Env Doc](https://virtualenv.pypa.io/en/latest/)

If you have pip and you want install virtualenv. Just open terminal and work this script "`pip install virtualenv`"

### If you want to use this structure, To follow this steps.

- Open terminal.
- Work this code `git clone https://github.com/Filiphasan/flask_rest_structure.git`
- This code clone this structure into your local machine.
- Open this project with VS Code or reletad Editör.
- Create `.env` file in current directory. Fill the `.env` file looking at the `.env.example` file.
- Open terminal and work `virtualenv env`.
- If succesfully created env folder, work this code for Windows `.\env\Scripts\activate` and for Linux `source env/bin/activate` on terminal for activate virtual environment.
- You create a virtual environment for your project.
- Work this code and install all dependencies `pip install -r requirements.txt`.

### How To Use Flask Migrate
- Change entity model class or create a new entity class
- Run this code `flask db migrate -m "Migration Name"`
- This code create new python file in migrations/versions folder.
- Run this code `flask db upgrade` and your db is update.