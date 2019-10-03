# Import the Flask app object
from app import app, db

# Set pre-import variables for the 'flask shell' context beyond
# the 'app' object using the decorator below for easy debugging in the REPL
@app.shell_context_processor
def make_shell_context():
    return {'db': db }

# Start the web server (in debug mode)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
