import os
from flask import Flask,jsonify,request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def ReturnJSON():
    data = {
        "Modules" : 15,
        "Subject" : "Data Structures and Algorithms",
    }
  
    return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
