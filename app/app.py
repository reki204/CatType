from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") 
def index():
  return render_template('index.html')

@app.route("/result") 
def result():
  return render_template('result.html')

# @app.route("test")
# def test():
#   return print('test')