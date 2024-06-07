from flask import Flask, render_template

app = Flask(__name__)

@app.route('/contact')
def contact():
    return render_template('contact.html')
