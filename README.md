
# [Hypothes.is](https://hypothes.is) feed server

This simple app serves up an Atom feed of posts to a given
[hypothes.is](https://hypothes.is) group.  This is useful for e.g. allowing
group members to receive updates to their email rather than having to check
the group stream regularly.


## Setup and running the app

### Local

The following assumes you have Python, pip, and virtualenv already installed.

  1. Copy the file `config.example.py` to `config.py`, and edit the settings inside.
  2. Create a new virtual environment in the `hypothesis-feed` directory with `virtualenv venv`
  3. Activate it with `source venv/bin/activate`.
  4. Install the required packages using `pip install -r requirements.txt`.
  5. Run the app with `python app.py`.
  
Repeat steps 3-5 whenever you want to run the app.

### Allowing others to access the feed

There are a number of ways to do this.  The simplest is perhaps to follow the
local instructions and use [ngrok](https://ngrok.com/) to set up a public URL.
However, the local development server is not designed to be used in this way,
so this is advisable only for testing purposes.

Many other services are available to run Python apps on the web.  In general,
you'll need some kind of WSGI setup to run the app.
[Python anywhere](https://www.pythonanywhere.com/) is easy to use for this if
you don't have much experience (or just want a free/simple solution).  There are
many tutorials around for running Flask apps on there.

As in the local setup, you will have to copy `config.example.py` to `config.py`
and edit the settings inside before running the app.


## Notes and contributing

I made this module for a course I was taking some time ago, so it may be that
hypothes.is will add their own feed to groups and this will become redundant.

Also, I'm no longer running this myself for the course in question, so though it
works at the time of writing, I won't automatically notice any bugs or API
changes.  If you still use it and want me to fix it, just contact me or add an
issue here.  I'll try to get around to it as soon as I can.  Alternatively, you
can fix it yourself and submit a pull request.
