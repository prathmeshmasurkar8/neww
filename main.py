from flask import Flask, render_template, request
import subprocess

app = Flask(__name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-scraping', methods=['POST'])
def run_scraping():
    if request.method == 'POST':
        result = subprocess.getoutput('python Scrappingscript.py')
        return result
    else:
        return "Method not allowed"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
