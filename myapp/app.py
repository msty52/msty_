from flask import Flask, render_template, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/time')
def get_time():
    msk = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(msk).strftime('%H:%M:%S')
    return jsonify(time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
