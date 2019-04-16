
axes = []
for i in range(64):
    ax = 'ax' + str(i)
    axes.append(ax)


f, axes  = plt.subplots(8, 8, sharey=True)
for ax in axes:
    ax.plot(x,y)
    
