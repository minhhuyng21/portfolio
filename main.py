from flask import Flask , render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)