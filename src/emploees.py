import pandas as pd

data = {
    'Ім\'я': ['Анна', 'Борис', 'Віктор', 'Георгій', 'Дмитро'],
    'Відділ': ['Продажі', 'Маркетинг', 'Продажі', 'Розробка', 'Маркетинг'],
    'Зарплата': [70000, 60000, 80000, 75000, 65000]
}
df = pd.DataFrame(data)

sorted_df = df.sort_values(by=['Відділ', 'Зарплата'], ascending=[True, False])

print(sorted_df.to_string(index=False))