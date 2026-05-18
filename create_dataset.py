import pandas as pd

data = {
    'SolarVoltage': [18,20,16,21,19],
    'BatteryVoltage': [12,12.5,11.8,13,12.2],
    'SunlightIntensity': [850,920,700,980,870],
    'MotorRPM': [3000,3200,2800,3400,3100],
    'LoadWeight': [5,4,6,3,5],
    'Temperature': [35,33,38,30,34],
    'BatteryUsage': [22,20,28,18,23],
    'Speed': [18,20,15,24,19],
    'Efficiency': [88,91,75,94,86]
}

df = pd.DataFrame(data)

df.to_csv('rover_data.csv', index=False)

print("CSV file created successfully!")