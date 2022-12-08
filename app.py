import os

import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_cors import cross_origin

from Prediction.predictFromModel import prediction
from Training.trainingModel import trainModel

app = Flask(__name__)

app.config["csv_file"] = "Prediction_Output_File/"
app.config["sample_file"] = "Prediction_SampleFile/"


@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')


@app.route('/return_sample_file/')
@cross_origin()
def return_sample_file():
    sample_file = os.listdir("Prediction_SampleFile/")[0]
    return send_from_directory(app.config["sample_file"], sample_file)


@app.route('/return_file/')
@cross_origin()
def return_file():
    final_file = os.listdir("Prediction_Output_File/")[0]
    return send_from_directory(app.config["csv_file"], final_file)


@app.route('/result')
@cross_origin()
def result():
    return render_template('result.html')


@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    if request.method == 'POST':
        try:
            if 'csvfile' not in request.files:
                return render_template("invalid.html")
            file = request.files['csvfile']
            df = pd.read_csv(file, index_col=[0])
            path = 'Prediction_InputFileFromUser/'
            # if os.path.isfile('Prediction_InputFileFromUser/InputFile.csv'):
            # os.remove('Prediction_InputFileFromUser/InputFile.csv')
            df.to_csv('Prediction_InputFileFromUser/InputFile.csv')
            pred = prediction()  # object initialization
            pred.predictionFromModel()
        except Exception as e:
            return render_template("invalid.html")
    return redirect(url_for('result'))


@app.route("/predictOne", methods=['POST'])
def predictOnetoOne():
    if request.method == 'POST':
        age = request.form['age']

        sex = request.form['sex']

        TSH = request.form['TSH']

        TT4 = request.form['TT4']

        FTI = request.form['FTI']

        T3 = request.form['T3']

        T4U = request.form['T4U']

        on_thyroxine = request.form['on_thyroxine']

        on_antithyroid_medication = request.form['on_antithyroid_medication']

        goitre = request.form['goitre']

        hypopituitary = request.form['hypopituitary']

        psych = request.form['psych']

        query = [age, sex, TSH, TT4, FTI, T3, T4U, on_thyroxine, on_antithyroid_medication, goitre, hypopituitary,
                 psych]

        pred = prediction()  # object initialization

        pred.predictionFromModelOnetoOne(query)

    return ""


@app.route('/train')
def train():
    print("Training")
    train = trainModel()
    train.trainingModel()
    print("Training comleted")


if __name__ == '__main__':
    app.run(debug=True)
