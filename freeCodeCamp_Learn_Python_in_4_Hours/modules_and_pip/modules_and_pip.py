# A module is a python file imported into our current python file. 
    # You would be able to access the variables and fuctions defined in that file in the current one you work on.
import random_stuff_for_modules # We can now access the variables, lists, or functions defined in the other file.
print(random_stuff_for_modules.roll_dice(10))

# You can actually get a list of python modules online.
    # https://docs.python.org/3/py-modindex.html
    # Modules are necessary because you can import code instead of having to write it out each time.

# There are built in modules and external modules.
    # BIMs are integrated into the python language.
    # External modules are stored in the folder where python is installed on our computers.
        # There should be a folder "Lib" under the Python installation in "External Libraries". (This is for Windows)
        # This is where you access the list of external modules.

# Third party modules can be found online as well.
    # This is where we use pip to help us install these modules.
    # To check if pip is preinstalled we open Terminal on Mac (CMD Prompt on Windows).
    # Type pip OR pip3 --version

# When third party modules are installed, they will be under folder "site-packages" in "Lib" (Windows).