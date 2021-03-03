# Personal-Website
Django version of my personal website

# Get Started

### Windows 

- Install python on your system [Python for Windows](https://www.python.org/downloads/windows/)
- Install virtualenv using pip3
  
```
pip3 install virtualenv
virtualenv <virtual_env_name>
<virtual_env_name>\Scripts\activate
```

### Debian-based Linux

- Install python3 and pip3 on your system.

```
sudo apt-get install python3
sudo apt-get install python3-pip   
```
- Install virtualenv using pip3 

```
sudo pip3 install virtualenv
virtualenv <virtual_env_name>
source <virtual_env_name>/bin/activate
```

### How to install Django

```
  pip3 install django
```

### Run Server in local machine
- Run server ``` python3 manage.py runserver ```
- Go to localhost http://localhost:8000

### Project Tree

```bash
├───pages
│   ├───migrations
│   │   └───__init__.py
│   ├───static
│   │   └───pages
│   │       ├───css
│   │       ├───images
│   │       └───js
│   ├───templates
│   │   └───pages
│   │       ├───about.html
│   │       └───base.html
│   │   
│   ├───__init__.py
│   ├───admin.py
│   ├───apps.py
│   ├───models.py
│   ├───tests.py
│   ├───urls.py
│   └───views.py
├───portfolioweb
│   ├───__init__.py
│   ├───asgi.py
│   ├───settings.py
│   ├───urls.py
│   └───wsgi.py
├───.gitignore
├───README.md
└───manage.py
```
