import os
from flask import Flask, render_template


app = Flask(__name__)

bgcolor="red"
# bgcolor= os.environ.get("BG_COLOR")

@app.route('/')
def hello():
    return render_template('index.html', bgcolor=bgcolor)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)