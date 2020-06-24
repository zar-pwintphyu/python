from flask import Flask
import pandas as pd 
#calendartest.py imports
from calendartest import mmdata
from calendartest import holiday


app = Flask(__name__)
#calendartest.py
#umc function with using GET 
@app.route('/', methods=['GET'])
def mm():
    return 'hey everyone!' #  Function from your calendartest.py

@app.route('/mm', methods=['GET'])
def get_mm():
    return mmdata #  Function from your calendartest.py

#umch function with using GET 
@app.route('/mm/mmh', methods=['GET'])
def get_mmh():
    return holiday #  Function from your calendartest.py




if __name__ == '__main__':
    app.run(debug=True)