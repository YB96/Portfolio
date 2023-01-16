from flask import Flask, render_template, jsonify

app = Flask(__name__)

Projects = [{
  'id':
  1,
  'title':
  'Exploratory Data Analysis on Brazilian E-Commerce Olist',
  'Libraries':
  'Pandas, Numpy, Matplotlib, Seaborn, Plotly',
  'link':
  'https://jovian.com/outlink?url=https%3A%2F%2Fjovian.ai%2Fyashchamp96%2Fproject-2-exploratory-data-analysis'
}, {
  'id':
  2,
  'title':
  'Exploratory Data Analysis and Visualization of Breast Cancer Data',
  'Libraries':
  'Pandas, Numpy, Matplotlib, Seaborn, Plotly',
  'link':
  'https://jovian.com/yashchamp96/course-project-on-breast-cancer'
}, {
  'id':
  3,
  'title':
  'Automated Web scraping project of Flipkart',
  'Libraries':
  'Pandas, Numpy, Selenium, AWS, Beautifulsoup',
  'link':
  'https://jovian.com/outlink?url=https%3A%2F%2Fjovian.ai%2Fyashchamp96%2Fproject-web-scraping'
}, {
  'id': 4,
  'title': 'Prediction using Machine Learing of Bulldozers',
  'Libraries':
  'Pandas, Numpy, Scikit-lear, Matplotlib, Plotly, Randomforest Regression',
  'link': 'https://jovian.com/yashchamp96/project-3-ml'
}]


@app.route("/")
def home():
  return render_template('home.html', project=Projects)


@app.route("/portfolio")
def portfolio():
  return render_template('portfolio.html')


@app.route("/api/projects")
def list_jobs():
  return jsonify(Projects)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
