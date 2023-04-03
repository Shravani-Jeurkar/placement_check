from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
# print(model)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    data = [int(x) for x in request.form.values()]
    # print(list(request.form.values()))
    val = model.predict([data])
    val_str = ''
    if val == 0:
        val_str = "You need to prepare well!!"
    
    elif val == 1:
        val_str = "All the very best, you are doing well!!"
    
    else:
        val_str = "Something went wrong! Try again later."

    return render_template('index.html', prediction_text = '{}'.format(val_str))

if __name__ == '__main__':
    app.run()