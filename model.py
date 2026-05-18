import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

# Load dataset
data = pd.read_csv('rover_data.csv')

# Features
X = data[[
    'SolarVoltage',
    'BatteryVoltage',
    'SunlightIntensity',
    'MotorRPM',
    'LoadWeight',
    'Temperature'
]]

# Targets
y = data[['BatteryUsage', 'Speed', 'Efficiency']]

# Train model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)

# Save model
pickle.dump(model, open('rover_model.pkl', 'wb'))

print("Rover model created successfully!")