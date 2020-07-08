# Black&White Image Coloriser


First of all make sure that python is installed in your system.

next, you need to create a virtual environment in your system of python and need to install the dependancies and packages which are gievn in the requirements.txt file by typing
the following command in the virtual environmant terminal</b>

## INSTALLING PIP

### Windows
The Python installers for Windows include pip. You should be able to access pip using:

<code>py -m pip --version</code>
<code>pip 9.0.1 from c:\python36\lib\site-packages (Python 3.6.1) </code>

You can make sure that pip is up-to-date by running:<br>
<code>py -m pip install --upgrade pip</code>

### Linux and macOS
<code>python3 -m pip install --user --upgrade pip</code>
Afterwards, you should have the newest pip installed in your user site:<br>

<code>python3 -m pip --version</code><br>
<code>pip 9.0.1 from $HOME/.local/lib/python3.6/site-packages (python 3.6)</code>

## Installing virtualenv

### On macOS and Linux:<br>
<code>python3 -m pip install --user virtualenv</code>

### On Windows:
<code>py -m pip install --user virtualenv</code>


## Creating a virtual environment
### On macOS and Linux:

<code>python3 -m venv env</code>
### On Windows:
<code>py -m venv env</code>


## Activating a virtual environment

### On macOS and Linux:
<code>source env/bin/activate</code>

### On Windows:
<code>.\env\Scripts\activate</code>
<br>

### Now your virtual environment has been created and you ready to install the packages required for the preject
<code>pip install -r requirements.txt --ignore-installed</code>
<br>
<br>

Now, you need to downlaod the pretrained model for the image coloriser which is available in the following link given below
https://bit.ly/3ecwq4m

the downloaded model should be placed in the model folder in the repopsitory  for the code to work


The model will would work somewhat in the given manner

![input and output images](https://user-images.githubusercontent.com/46163555/71523947-43c03a00-2899-11ea-8943-e8db1347c7f5.jpg)
![input and output images](https://user-images.githubusercontent.com/46163555/71523948-4458d080-2899-11ea-8a8a-d54fbf39c9b8.jpg)


