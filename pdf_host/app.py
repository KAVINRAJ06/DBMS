from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # Redirect straight to your PDF in static folder
    return redirect(url_for('static', filename='Data Base Management System (1).pdf'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
