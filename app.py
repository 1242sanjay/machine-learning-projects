from flask import Flask, render_template, request
import pickle
import pandas
from book_recommendation import book_recommender

popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('home.html')


@app.route('/projects')
def projects():
  return render_template('projects.html')


@app.route('/recommendation')
def recommendation():
  return render_template('recommendation.html',
                         book_name=list(popular_df['Book-Title'].values),
                         author=list(popular_df['Book-Author'].values),
                         image=list(popular_df['Image-URL-M'].values),
                         votes=list(popular_df['num_rating'].values),
                         rating=list(popular_df['avg_rating'].values))


@app.route('/recommend_book', methods=['post'])
def recommend_book():
  user_input = request.form.get('user_input')
  book_dict = book_recommender(user_input)
  return render_template('recommendation.html',
                         book_title=book_dict['book_title'],
                         book_author=book_dict['book_author'],
                         book_image=book_dict['book_image'])


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
