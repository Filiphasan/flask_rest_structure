# Flask Restful New Project Structure

>This repository is structure to start a new flask restful project. Contains enter and mid level project.

>**This structure is done, but still continues to be developing!**

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
- `.env` file has two attributes. First one is PostgreSQL Connection string. Second one is project secret key.
- Edit Connection string for your local or remote postgresql database connection. Database must be already created.
- Add secret key (string) for jwt symetric security key etc.
- Open terminal and work `virtualenv env`.
- If succesfully created env folder, work this code for Windows `.\env\Scripts\activate` and for Linux `source env/bin/activate` on terminal for activate virtual environment.
- You should seen like this string on your terminal. This is proof of virtual env is working.
```
(env) PS C:\Users\sa\Desktop\WebApp\Python\Flask\flask-rest-structure>
```
- You create and active a virtual environment for your project.
- Work this code and install all dependencies `pip install -r requirements.txt`.
- This code install all dependencies in `env/Lib` folder. After install finish, you seen all dependencies in `env/Lib` folder.
- Open terminal and run `flask db upgrade` and created users table in your db.
- After you ready for work this project.
- Open terminal on project current directory. Run `python app.py` and seen this.
```
(env) PS C:\Users\sa\Desktop\WebApp\Python\Flask\flask-rest-structure> python app.py
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 190-640-651
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
- This project running on `http://127.0.0.1:5000/` or `http://localhost:5000/` both of same.
- `http://localhost:5000/api` is current url path.
- Swagger doc path is `http://127.0.0.1:5000/api/doc`, like this.
![Swagger Document](https://i.ibb.co/fDct42m/Ekran-g-r-nt-s-2022-01-01-144949.png)

### How To Use Flask Migrate
- If don't have migrations folder. Run `flask db init`. Created migrations folder.
- Change entity model class or create a new entity class
- Run this code `flask db migrate -m "Migration Name"`
- This code create new python file in migrations/versions folder.
- Run this code `flask db upgrade` and your db is update.