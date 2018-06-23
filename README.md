
# Hypothes.is feed generator

This simple app serves up an Atom feed of posts to a given [hypothes.is](https://hypothes.is) group.

I made this module for a course I was taking some time ago, so it may be that hypothes.is will add their own feed to
groups and this will become redundant.

Also, I'm no longer running this myself for the course in question, so though it works at the time of writing, I won't
automatically notice any bugs or API changes.  If you still use it and want me to fix it, just contact me or add an
issue here.  I'll try to get around to it as soon as I can.  Alternatively, you can fix it yourself and submit a pull
request.


## Setup

[Flask](http://flask.pocoo.org/) is used to serve the feed, so you'll need some kind of WSGI setup to run the app.
[Python anywhere](https://www.pythonanywhere.com/) is easy to use for this if you don't have much experience (or just
want a free/simple solution).  There are many tutorials around for running Flask apps on there.

Required packages are listed in the requirements.txt file, and can be installed with `pip install -r requirements.txt`
if you need to do this manually.