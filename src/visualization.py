import os
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Товар': ['Товар A', 'Товар B', 'Товар A', 'Товар C', 'Товар B', 'Товар C'],
    'Регіон': ['Регіон 1', 'Регіон 2', 'Регіон 1', 'Регіон 2', 'Регіон 1', 'Регіон 2'],
    'Продажі': [150, 200, 100, 300, 250, 400]
}

df = pd.DataFrame(data)

grouped_data = df.groupby(['Регіон', 'Товар'])['Продажі'].sum().reset_index()

pivot_data = grouped_data.pivot(
    index='Регіон',
    columns='Товар',
    values='Продажі'
)

pivot_data.plot(kind='bar')

plt.title('Сумарні продажі товарів по регіонах')
plt.xlabel('Регіон')
plt.ylabel('Продажі')
plt.xticks(rotation=0)
plt.legend(title='Товар')
plt.tight_layout()

image_dir = 'resources/images'
os.makedirs(image_dir, exist_ok=True)

image_path = os.path.join(image_dir, 'sales_by_region.png')

plt.savefig(image_path)

plt.show()
