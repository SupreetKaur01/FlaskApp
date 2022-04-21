"""test Flask with this"""

from flask import Flask,render_template
from twitterAnalyzer import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bitcoin')
def bitcoin_analyzer():
    tweetsAnalyzeVisualization('bitcoin',100)


@app.route('/ethereum')
def ethereum_analyzer():
        return render_template('bitcoin-visualization.html')

if __name__ == '__main__':
    app.run(debug=True)