import sklearn.datasets
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB


train_data = sklearn.datasets.load_files(container_path='train_data',
                                         load_content=True,
                                         encoding='utf-8')

text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB())])

text_clf = text_clf.fit(train_data.data, train_data.target)

test_data = sklearn.datasets.load_files(container_path='test_data',
                                        load_content=True,
                                        encoding='utf-8')

predicted = text_clf.predict(test_data.data)

print(metrics.classification_report(test_data.target, predicted,
                                    target_names=test_data.target_names))
