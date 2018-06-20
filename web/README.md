# Princeton Prowl

Princeton Prowl is the app for students to find others in the same courses to
form study groups. Just login with CAS, add your courses and find groups.

## Getting Started

This is an entirely open-source project that you can download and play around
with. These instructions give the most direct path to setting up and getting
oriented. Unfortunately we only have instructions for macOS but any \*nix system
should be virtually identical.

#### macOS

First, download the project here on GitHub. You primarily need
[Python 3](https://www.python.org/downloads/) which
is easily installed with the macOS package manager [Homebrew](https://brew.sh/)
(which you need to install as well):

    brew install python3

Once installed, go to the project directory and start the Python 3 virtual
environment with:

    source bin/activate

Exit the virtual environment with 'deactivate'.

Then, in order to install all the required Python packages run:

    pip3 install -r requirements.txt

Next, setup a mySQL database and configure the database settings in
/settings/base.py to match your mySQL configurations.

You can use the reset-db bash script to setup the database and do the initial
migration, just run it:

    bash ~/bin/reset-db.sh
