'''
Задача №65. Решение в группах
Написать EDA для датасета про пингвинов
Необходимо:
● Использовать 2-3 точечных графика
● Применить доп измерение в точечных графиках, используя
аргументы hue, size, style
● Использовать PairGrid с типом графика на ваш выбор
● Изобразить heatmap
● Использовать 2-3 гистограммы
'''

from seaborn import load_dataset, scatterplot, PairGrid, heatmap
from matplotlib.pyplot import show

data = load_dataset("penguins")

# # scatterplot(data=data, x="flipper_length_mm", y="body_mass_g")
# scatterplot(data=data, x="flipper_length_mm", y="body_mass_g", hue="sex", size="island", style="island")
# x_vars = ["body_mass_g", "bill_length_mm", "bill_depth_mm",
#           "flipper_length_mm"]
# y_vars = ['sex']
# g = PairGrid(data, x_vars=x_vars, y_vars=y_vars, hue="species")
# g.map(scatterplot)

# penguins = data.pivot_table(index="species", columns="island", values="body_mass_g")
# heatmap(penguins)




show()

