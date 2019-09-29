# import os
import requests
import urllib.parse
import json

from flask import redirect, render_template, request, session
from functools import wraps

def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def location():
    """Look up for locations in Nigeria."""

# Contact API
    try:
        with open('statecities.json', 'r') as f:
            content = json.load(f)

    except requests.RequestException:
        return None

    # Parse response
    try:
        location = content
        return location
    except (KeyError, TypeError, ValueError):
        return None

#!/usr/bin/env python3
def naira(value):
    """Format value as Naira."""
    return f"₦{value:,.2f}"
# print(naira(100000000))
