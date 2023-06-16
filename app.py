# print(__name__) how a paticular script is invoked

from flask import Flask

app = Flask(__name__)

@app.route("/")  # decorator @app applied to home page
def helloworld():
  return "Welcome to Priyanka World"

if __name__=="__main__": 
  app.run(host='0.0.0.0',debug=True)  

