from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
import pymssql

@app.route('/', methods=['GET'])
def home():
    return render_template()






if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)