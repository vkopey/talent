# -*- coding: utf-8 -*-
from bottle import route, run, request
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

x=np.array([[5,5,4,3,4,5,5,5,5,5, 3,2,3,3,4,3,4,3,3,3], # математика
            [4,3,3,3,4,2,3,3,4,3, 5,5,4,4,5,5,5,5,5,4]]) # укр. мова
y=np.array( [0,0,0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1,1,1] ) # мітки класів (бінарна класифікація)
y_names={0:"технарь", 1:"гуманітарій"}
x=x.T
model=RandomForestClassifier(n_estimators=5, max_depth=3) # модель
model.fit(x, y) # виконати навчання

@route('/') # http://localhost:8080
def form():
    return """Введіть ваші оцінки: <form action="/edit" method="post">
1. Математика <input type="text" name="x1"> <br>
2. Українська мова <input type="text" name="x2"> <br>
3. Фізика <input type="text" name="x3"> <br>
<input type="submit" value="Submit" /></form>
"""

@route('/edit', method='POST')
def hello_post():
    x1=int(request.POST['x1'])
    x2=int(request.POST['x2'])
    y=model.predict([[x1, x2]]) # прогноз
    y=y[0]
    r='Ви, швидш за все, '+y_names[y]+'!'
    return r

run(host='localhost', port=8080)