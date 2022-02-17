from pylab import*
x=arange(0,15,0.01)
y=lambda x: x**5 + 5
plot(x,y(x))
show()
