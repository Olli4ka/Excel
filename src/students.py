import pandas as pd

data = {
    'Ім\'я студента': ['Іванов', 'Петров', 'Сидоров'],
    'Середній бал': [4.5, 3.7, 4.2]
}
df = pd.DataFrame(data)

df.to_excel('resources/excel_files/students.xlsx', sheet_name='Група 1', index=False)