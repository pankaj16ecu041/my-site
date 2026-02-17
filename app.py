from flask import Flask

# Create a Flask application instance.
# __name__ helps Flask determine the root path of the application
# so it can locate resources like templates and static files.
app = Flask(__name__)

# The route() decorator binds a URL path to a Python function.
# When a user visits the root URL ('/'), the 'hello_world' function is called.
@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

# This conditional ensures the development server runs only when the script is
# executed directly, not when imported as a module.
if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)