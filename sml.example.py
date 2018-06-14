#!/usr/bin/python3

import sklearn
from sklearn import tree

#features of apple and orange
# here 0 is smooth and 1 is bumpy
data=[[100,0],[130,0],[135,1],[150,1]]
output=["apple","apple","orange","orange"]

# call decision tree algo
algo=tree.DecisionTreeClassifier()

#train data
trained_algo=algo.fit(data,output)

#now testing phase
predict=trained_algo.predict([[126,1]])

#printing output
print(predict)
