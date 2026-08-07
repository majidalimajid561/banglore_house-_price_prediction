# app/__init__.py
# GOAL: This file is the "Electrical Panel" of your house.
# It creates the central Flask application and tells it where to find everything.
# It runs ONCE when your server starts.

from flask import Flask

def create_app():
    """
    This is a "Factory Pattern". Instead of creating the app globally,
    we create it inside a function. This is the GOOD WAY because it allows
    multiple configurations and easier testing.
    """
    # 1. Create the actual Flask web application.
    # __name__ is a Python special variable that tells Flask where to look
    # for templates (HTML) and static (CSS/JS) files.
    app = Flask(__name__)

    # 2. Import the "routes" (URLs) from the routes.py file.
    # We do this here so that when the server starts, Flask knows:
    #    "When someone goes to '/' -> call the home() function".
    # The '.routes' means "look for a file named routes.py in the same folder".
    from . import routes
    
    # 3. Connect the routes to the app.
    # bp stands for "Blueprint" (a group of routes). We register it.
    app.register_blueprint(routes.bp)

    # 4. Return the fully created app so that run.py can start it.
    return app