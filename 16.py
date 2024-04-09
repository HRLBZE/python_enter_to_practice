from matplotlib import pyplot as pl

x=[1,2,3,4]
pl.style.use('seaborn')
fig,ax=pl.subplots()
ax.plot(x,color='red')
fig.show()
