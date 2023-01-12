from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'Location': 'Bengaluru, India',
  'Salary': 'Rs. 15 Lac'
}, {
  'id': 2,
  'title': 'Data Analyst',
  'Location': 'Pune, India',
  'Salary': 'Rs. 5 Lac'
}, {
  'id': 3,
  'title': 'Data Associate',
  'Location': 'Bengaluru, India',
  'Salary': 'Rs. 7 Lac'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
