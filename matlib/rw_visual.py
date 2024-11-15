import matplotlib.pyplot as plt 

from random_walk import RandomWalk

while True:
    rw = RandomWalk(5_000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    #ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = input("Make another wlak? (y/n):")
    if keep_running.lower() == 'n':
        break