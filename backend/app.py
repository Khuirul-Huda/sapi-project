from bottle import Bottle, run, route, request
import pickle

model = pickle.load(open('modeldata.pkl', 'rb'))

@route('/predict', method='POST')
def predict():
    url = request.forms.post('url')
    predict = model.predict(['youtube.com'])
    return {"url": str(url), "predict": str(predict[0])}

run(app, host='localhost', port=8080)
