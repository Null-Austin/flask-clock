from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    file=open('clock.html')
    return file.read()
app.run()