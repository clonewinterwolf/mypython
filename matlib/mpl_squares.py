import matplotlib.pyplot as plt

input_values =[1, 2, 3, 4, 5]
squares = [1, 4, 9, 16,25]
plt.style.use('grayscale')
fig, ax = plt.subplots()  #fig represent the entire figure. 

ax.plot(input_values, squares, linewidth=3)

#set the chart
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("square of Value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)

plt.show()