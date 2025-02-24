from flask import Flask, jsonify
from flask_cors import CORS

from ModList import ModList, Mod

app = Flask(__name__)
app.config.from_object(__name__)

modlist: ModList = ModList()

#CORS(app, resources={r"/*":{'origins':"*"}})
CORS(app, resources={r"/*":
                     {'origins':'http://localhost:5173',
                      "allow_headers":"Access-Control-Allow-Origin"
                      }})

#hello world route
@app.route('/', methods=['GET'])
def greetings():
    return jsonify("Hello, World!")

@app.route('/shark', methods=['GET'])
def shark():
    return jsonify("This is a Shark and you are too!")

@app.route('/modlist', methods=['GET'])
def view_modlist():
    return jsonify(modlist.getModList())

if __name__ == "__main__":
    app.run(debug=True)