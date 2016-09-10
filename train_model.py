import sklearn.datasets


train_data = sklearn.datasets.load_files(container_path='train_data',
                                         load_content=True,
                                         encoding='utf-8')

print len(train_data.target)
