
LordMike's helpfull Python script toys
======================================


( Guide is under construction :)


This project contains Python script functions.
These functions can be used by other script :)

Add this project as submodule to other projects:

.. code-block:: bash

 $ git submodule add https://github.com/lordmikefin/LMToyBoxPython.git LMToyBoxPython

Usefull git commands:

.. code-block:: bash
 
 # Change remote point to ssh. Run within submodule.
 $ git remote -v
 $ git remote set-url origin git@github.com:lordmikefin/LMToyBoxPython.git
 
 # Init & upadte the project submodules. Run within main project.
 $ git submodule init
 $ git submodule update
 
 # Pull whole main project and all submodules. Run within main project.
 $ git pull
 $ git submodule foreach "(git checkout master; git pull)"
