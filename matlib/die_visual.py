from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)
results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

#print(results)
#analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#visualize the result
x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title="Result of rolloing three d6 5000 times", xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_x3.html')
