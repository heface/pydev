#-*- coding=utf-8 -*-
from sklearn.datasets import fetch_20newsgroups
news = fetch_20newsgroups(subset='all')
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(news.data,news.target,test_size=0.25,random_state=33)
from sklearn.feature_extraction.text import CountVectorizer
count_vec = CountVectorizer()
X_count_train = count_vec.fit_transform(X_train)
X_count_test = count_vec.transform(X_test)
from sklearn.naive_bayes import MultinomialNB
mnb_count = MultinomialNB()
mnb_count.fit(X_count_train,Y_train)
