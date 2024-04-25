from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inner-page')
def inner_page():
    return render_template('inner-page.html')

@app.route('/portfolio-details')
def portfolio_details():
    return render_template('portfolio-details.html')

@app.route('/static')
def serve_static(filename):
    directory = os.path.join(app.static_folder, os.path.dirname(filename))
    file = os.path.basename(filename)
    return send_from_directory(directory, file)

if __name__ == '__main__':
    app.run(debug=True)
