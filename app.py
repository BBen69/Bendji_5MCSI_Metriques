from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <h1>Welcome to Flask App</h1>
        <form action="/install">
            <button type="submit">Install Application</button>
        </form>
    ''')

@app.route('/install')
def install():
    return "Application Installed!"

if __name__ == '__main__':
    app.run(debug=True)
