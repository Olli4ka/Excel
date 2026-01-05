import pandas as pd

data = {
    'Фрукти': ['Яблуко', 'Банан', 'Вишня'],
    'Кількість': [10, 5, 2]
}
df = pd.DataFrame(data)

df.to_excel('resources/excel_files/fruits.xlsx', sheet_name='Улюблені фрукти', index=False)

print("Дані успішно записано у файл 'fruits.xlsx'")