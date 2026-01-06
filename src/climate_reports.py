import pandas as pd
from random import randint

def generate_data():
    return {
        'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'temperature_source_1': [randint(20, 30) for _ in range(7)],
        'humidity_source_1': [randint(50, 70) for _ in range(7)],
        'temperature_source_2': [randint(20, 30) for _ in range(7)],
        'humidity_source_2': [randint(50, 70) for _ in range(7)]
    }

data = generate_data()
df = pd.DataFrame(data)

with pd.ExcelWriter('resources/excel_files/climate_reports.xlsx') as writer:
    for day in data['day']:
        df[df['day'] == day].to_excel(writer, sheet_name=day, index=False)