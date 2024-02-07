'''
Дан файл california_housing_train.csv. Определить среднюю стоимость дома ,
где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
Используйте модуль pandas.
'''

# Введите ваше решение ниже

import pandas as pd
df = pd.read_csv("california_housing_train.csv") # Тот же файл california_housing_test.csv, но в таком виде получен от преподавателя

filtered_df = df[(df["population"] >= 0) & (df["population"] <= 500)]
avg = filtered_df["median_house_value"].mean()

# или

df = pd.read_csv('california_housing_train.csv')
avg = df[(df['population'] > 0) & (df['population'] < 500)]['median_house_value'].mean()  # Средняя стоимость дома, где количество людей от 0 до 500


