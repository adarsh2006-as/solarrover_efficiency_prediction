from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open('rover_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    SolarVoltage = float(request.form['SolarVoltage'])
    BatteryVoltage = float(request.form['BatteryVoltage'])
    SunlightIntensity = float(request.form['SunlightIntensity'])
    MotorRPM = float(request.form['MotorRPM'])
    LoadWeight = float(request.form['LoadWeight'])
    Temperature = float(request.form['Temperature'])

    data = pd.DataFrame({
        'SolarVoltage': [SolarVoltage],
        'BatteryVoltage': [BatteryVoltage],
        'SunlightIntensity': [SunlightIntensity],
        'MotorRPM': [MotorRPM],
        'LoadWeight': [LoadWeight],
        'Temperature': [Temperature]
    })

    prediction = model.predict(data)

    battery = round(prediction[0][0], 2)
    speed = round(prediction[0][1], 2)
    efficiency = round(prediction[0][2], 2)

    return render_template(
        'index.html',
        battery=battery,
        speed=speed,
        efficiency=efficiency
    )

if __name__ == '__main__':
    app.run(debug=True)