# Installing the virtual environment

In general, it is bad practice to have packages for these projects installed at a global level.

As such, we will work in a "virtual environment"

## Installation of `pipenv`

`pipenv` functions as a virtual environment for installing and "locking" different packages in place. This will mitigate potential package mistmatching/dependency issues from installing globally. Its documentation is located on the [pipenv website](https://pipenv.pypa.io/en/latest/)

First, open your favorite flavor of Terminal (probably Ubuntu or Powershell), and type the following:
`pip install --user pipenv` (this is assuming you have > Python 3.8)
