import pickle
import pandas
import numpy as np

pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))


def book_recommender(book_name):
  suggations = {"book_title": [], "book_author": [], "book_image": []}
  index = np.where(pt.index == book_name)[0][0]
  similar_items = sorted(list(enumerate(similarity_scores[index])),
                         key=lambda x: x[1],
                         reverse=True)[1:9]
  for i in similar_items:
    temp_df = books[books['Book-Title'] == pt.index[i[0]]]

    suggations['book_title'].extend(
      list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
    suggations['book_author'].extend(
      list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
    suggations['book_image'].extend(
      list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
  return suggations
