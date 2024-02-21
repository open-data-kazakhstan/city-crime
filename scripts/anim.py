import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
file_path = r'C:\Users\USER\Desktop\Практика\city-crime\data\comb.csv'
df = pd.read_csv(file_path)

# Создание графика пирога
fig, ax = plt.subplots(figsize=(12, 8))
wedges, texts, autotexts = ax.pie(df['Total_crimes'], labels=None, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.4), pctdistance=0.85)

# Установка местоположения текста внутри или снаружи пирога
ax.axis('equal')  # Убедитесь, что круг выглядит как круг
plt.title('Распределение правонарушений по регионам в 2022 году')

# Добавление легенды
legend = ax.legend(df['Region'], title='Регионы', bbox_to_anchor=(1, 0.5), loc="center right", bbox_transform=plt.gcf().transFigure)

# Изменение местоположения текста
for text, autotext in zip(texts, autotexts):
    text.set(size=10)  # размер текста
    autotext.set(size=8, color='white')  # размер и цвет текста с процентами
    autotext.set_horizontalalignment('center')  # выравнивание по центру

plt.tight_layout(rect=[0, 0, 0.85, 1])  # улучшение распределения местоположения графика в окне
plt.show()
