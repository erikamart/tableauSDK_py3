# Creating a Tableau Data Extract (.tde) file using Python 3.5.2 on Windows 10

![N|Solid](https://raw.githubusercontent.com/erikamart/tableauSDK_py3/master/py_sdk.png)

This repository includes files extracted from a zip file found at [tableau.com](https://onlinehelp.tableau.com/current/api/sdk/en-us/help.htm#SDK/tableau_sdk.htm%3FTocPath%3D_____1).  Overall step by step instructions on how to extract the files and get setup with Python can be followed from this youtube: ["Tableau Training & Tutorials 13 01 APIs Extract API Introduction"](https://www.youtube.com/watch?v=Oj2NUh03H4s).

#### Software Required
* [Python 3] - Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.
* [Tableau SDK] - The Tableau SDK contains a set of functions for creating Tableau Data Extract (.tde) files and for publishing extracts to a Tableau Server.

## Installation

  - Download and install Python 3.5.2 or later
  - Clone this repository if you have Windows 10. Otherwise, click the Tableau SDK link above to download the zipfile and extract the appropriate tableau SDK files for your system.
  - The extracted folder will be called `TableauSDK-10300.18.0703.1954` or something similar. Change directories into the folder.
  - Make sure you are running your CLI with administrator rights and have python run the `setup.py` file.

```sh
$ cd TableauSDK-10300.18.0703.1954
$ python setup.py install
```
  - The `trivialExample.py` file was created and added to the `TableauSDK-10300.18.0703.1954` folder of this repo (based from the youtube video linked above).  It was modified to work with python 3 because the original instructions in the video were for python 2 and would not work if left unchanged.  Note the changes in the file indicated with comments.  If you did not clone this repo, then copy the contents of the `trivialExample.py` file from [here](https://raw.githubusercontent.com/erikamart/tableauSDK_py3/master/TableauSDK-10300.18.0703.1954/trivialExample.py) into your own new file and save it inside your copy of the `TableauSDK-10300.18.0703.1954` folder.
  - Have python run the `trivialExample.py` file.

```sh
$ python trivialExample.py
```
  - If all ran sucessfully, you will see a new file called `trivialExample.tde` appear in the `TableauSDK-10300.18.0703.1954` folder.  This repo contains a copy of a [trivialExample.tde](https://github.com/erikamart/tableauSDK_py3/blob/master/trivialExample.tde) file resulting from completing the above instructions.


   [Python 3]: <https://www.python.org/getit/>
   [Tableau SDK]: <https://onlinehelp.tableau.com/current/api/sdk/en-us/SDK/tableau_sdk_installing.htm#downloading># tableauSDK_py3
