# Python examples
My notes for python code.
See sub folders for more information.

Notes
* Don't name the files same as the library you are using. For example `numpy.py`.

## Pip
Pip is the package manager for python.

This is how you can install django:
`pip install Django`

This method installs newer version of already existing package;
`pip install Django --upgrade`

And this is the short cut for upgrade:
`pip install Django -U`

This error indicates that you should try to install the package as as system administrator.
In Windows you can run cmd as an admin.
`PermissionError: [Errno 13] Permission denied: 'c:\\program files\\python36\\Lib\\site-packages\\six.py'`

## Modules, classes and packages
Class is an object abstraction.

Module is just a bunch of reusable python code.
It might include functions and classes.
Modules are imported with `import`.

Packages can thought as a set of modules having common namespace.
Then you can refer to a module inside a package like `package.module`.

## Virtual environment
**Create**
In Linux `virtualenv venv` where *venv* is the name of the virtual environment.

**Activate**
In Linux `source venv/bin/activate`

**Deactivate**
In Linux `deactivate`

**Destroy**
Remove the `venv` folder or whatever was the name of your virtual environment.

## Errors

`ModuleNotFoundError: No module named 'Cython'` when running `pip3 install -r requirements.txt`.

Try installing `Cython` and other error producing libraries by `pip3 install library` where _library_ is replaced by the library name.
