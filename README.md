# WHAT IS THIS?
Python webshop demo, based upon school assignment.

# COMPONENTS
* Python
* Flask (Python module)
* Bulma (CSS)

# REQUIREMENTS
* Python [Download](https://www.python.org/ftp/python/3.13.1/python-3.13.1-amd64.exe)
* Flask 

# HOW TO INSTALL
Download the above python, run the file, follow the wizard, reboot if necessary.
Open a terminal and make sure you can run Python, if its not working you need to add where python was installed to your environment PATH, google it.

When the above is working, install python virtual environment with `python -m pip install virtualenv`
Create the environment with `virtualenv venv`
Activate the environment with `.\venv\Scripts\activate.ps1`

Now we can install the requirements file inside the virtual environment

`pip install -r requirements.txt`

and now you should be able to run it with `python app.py`
