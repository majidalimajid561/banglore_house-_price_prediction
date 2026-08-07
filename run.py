# run.py
# GOAL: This is the "Ignition Key". 
# It creates the Flask app from app/__init__.py and runs the web server.
# You run this file to start your website.
import os
from app import create_app
# Create the Flask application (this calls the create_app() function we wrote in __init__.py)
app = create_app()

if __name__ == '__main__':
    # debug=True means:
    #   1. If you change any Python code, the server restarts automatically.
    #   2. If your code crashes, it shows a helpful debug page in the browser.
    # host='0.0.0.0' lets other devices on your network access your app.
    # port=5000 is the default Flask port.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)