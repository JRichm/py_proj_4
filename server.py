from flask import Flask

app = Flask(__name__)


        ##        Flask Routes        ##
@app.route('/')
def home():
    return "Project Tracking App"


        ##       Server Methods       ##
if __name__ == '__main__':
    app.run(debug=True)