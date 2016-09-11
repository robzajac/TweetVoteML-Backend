import sklearn.datasets
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression


train_data = sklearn.datasets.load_files(container_path='train_data',
                                         load_content=True,
                                         encoding='utf-8')

text_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
                     ('clf', LogisticRegression())])

text_clf = text_clf.fit(train_data.data, train_data.target)

test_data = sklearn.datasets.load_files(container_path='test_data',
                                        load_content=True,
                                        encoding='utf-8')

predicted = text_clf.predict(test_data.data)

print(metrics.classification_report(test_data.target, predicted,
                                    target_names=test_data.target_names))

print(metrics.accuracy_score(test_data.target, predicted))

# Dumping the model
filename = 'model/tweets_classifier.joblib.pk1'
_ = joblib.dump(text_clf, filename, compress=3)
