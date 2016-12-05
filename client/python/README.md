# FNTM API template Python code

## Get template code from GitHub or from source distribution

**GitHub**

```
git clone https://github.com/FunctionLab/fntm-api
cd fntm-api/client/python
```

**Source distribution**

```
wget http://fntm-api.princeton.edu/static/fntmapi-1.0.0.tar.gz
tar -xzvf fntmapi-1.0.0.tar.gz
cd fntmapi-1.0.0
```

## Install dependencies

The only external depedency required by the template code is the **requests** library. If this is already installed on your system, you can skip this section.

The recommended way of installing **requests** is in a virtual environment.

```
virtualenv env
source env/bin/activate
python setup.py install
```

Alternatively, you can install **requests** to the site-packages directory of your user account.

```
python setup.py install --user --prefix=
```

## Run template code

```
python fntmapi.py
```

This will run through a sequence of use cases illustrating the features of the API. A sample output is provided in `expected-output.txt`.
