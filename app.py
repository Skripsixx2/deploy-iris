from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

def load_model():
    global model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html', classIris="None")

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    Slength, Swidth, Plength, Pwidth  = [x for x in request.form.values()]

    data = []

    data.append(float(Slength))
    data.append(float(Swidth))
    data.append(float(Plength))
    data.append(float(Pwidth))
    
    prediction = model.predict([data])
    output = str(prediction[0])

    return render_template('index.html', classIris=output, Slength=Slength, Swidth=Swidth, Plength=Plength, Pwidth=Pwidth)


if __name__ == '__main__':
    load_model()
    app.run(debug=True)