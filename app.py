from flask import Flask, render_template
import json, sqlite3, datetime,requests
import scrapper

app = Flask(__name__)


@app.route("/")
def show_data():     
    return render_template('index.html')    

if __name__ == "__main__":
    app.run(debug=True)


