from flask import Flask, render_template, jsonify

app = Flask(__name__)

Projects = [{
  'id': 1,
  'title': 'Exploratory Data Analysis on Brazilian E-Commerce Olist',
  'Libraries': 'Pandas, Numpy, Matplotlib, Seaborn, Plotly'
}, {
  'id': 2,
  'title': 'Exploratory Data Analysis and Visualization of Breast Cancer Data',
  'Libraries': 'Pandas, Numpy, Matplotlib, Seaborn, Plotly'
}, {
  'id': 3,
  'title': 'Automated Web scraping project of Flipkart',
  'Libraries': 'Pandas, Numpy, Selenium, AWS, Beautifulsoup'
}, {
  'id': 4,
  'title': 'Sudoku Solver',
  'Libraries' : 'Pandas NumPy'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', project=Projects)


@app.route("/api/projects")
def list_jobs():
  return jsonify(Projects)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
