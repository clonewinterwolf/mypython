import matplotlib.pyplot as plt

x_values = range(1, 100)
y_values = [x*x*x for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='red', s=10)
#set the chart
ax.set_title("Cube numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)

#ax.axis([0,1100, 0,1100000])

plt.show()
