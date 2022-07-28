# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

# 3. define what to do when user goes to the /about route
if __name__ == "__main__":
    app.run(debug=True)
#     #app.run()