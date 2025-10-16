from flask import Flask

# Step 1: Create a Flask application
app = Flask(__name__)

# Step 2: Define a route (the URL the user visits)
@app.route('/')
def home():
    return "Hello from my first CI/CD project! 22"

# Step 3: Run the app
if __name__ == '__main__':
    # host='0.0.0.0' means it’s accessible from any machine (good for Docker)
    app.run(host='0.0.0.0', port=5000)
