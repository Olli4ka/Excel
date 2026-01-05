import pandas as pd

january_data = {
    'Книга': ['Пітон для всіх', 'Секрети JavaScript'],
    'Продажі': [50, 30]
}
january_df = pd.DataFrame(january_data)

february_data = {
    'Книга': ['Пітон для всіх', 'Секрети JavaScript'],
    'Продажі': [70, 40]
}
february_df = pd.DataFrame(february_data)

EXCEL_PATH = 'resources/excel_files/book_sales.xlsx'

with pd.ExcelWriter(EXCEL_PATH) as writer:
    january_df.to_excel(writer, sheet_name='Січень', index=False)
    february_df.to_excel(writer, sheet_name='Лютий', index=False)

print("Дані успішно записані у файл 'book_sales.xlsx'.")