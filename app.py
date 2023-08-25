# print(__name__) how a paticular script is invoked

from flask import Flask,render_template, jsonify

app = Flask(__name__)
JOBS=[{
  'Job_title': "Software Engineer",
  'Location': "New York",
  'Salary': "$1,00,000"
  },
  {
  'Job_title': "Data Engineer",
  'Location': "New York",
  'Salary': "$1,00,000"
  },
  {
  'Job_title': "Data Analyst",
  'Location': "New York",
  'Salary': "$1,00,000"
  }
  ]

@app.route("/")  # decorator @app applied to home page
def helloworld():
  return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")  # decorator @app applied to home page
def list_jobs():
  return jsonify(JOBS)

# @app.route("/api/home")
# def 

if __name__=="__main__": 
  app.run(host='0.0.0.0',debug=True)  

