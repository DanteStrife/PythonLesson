'''
Создать новый столбец в таблице с
пингвинами, который будет отвечать за
показатель длины клюва пингвина.
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)
'''


'''
Задача №69. Решение в группах
1. Изобразить гистограмму по flipper_length_mm
с оттенком height_group. Сделать анализ
'''
from pandas import read_csv
from seaborn import histplot
from matplotlib.pyplot import show
data = read_csv("penguins.csv")
#
# data.loc[data['bill_length_mm'] < 35, 'height_group'] = 'low'
# data.loc[data['bill_length_mm'] > 42, 'height_group'] = 'high'
# data.loc[(data['bill_length_mm'] > 35) & (data['bill_length_mm'] < 42), 'height_group'] = 'middle'
#
# data.to_csv("penguins.csv", index=False)

histplot(data, x="flipper_length_mm", hue="height_group")

show()
