import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-9,0,1)
y=-1/8*(x+9)**2+8
plt.plot(x,y,color='r',linestyle=':', marker='h',markersize=5, label='Jooniseis')
x=np.arange(1,10,1)
y=-1/8*(x-9)**2+8
plt.plot(x,y,color='r',linestyle=':', marker='h',markersize=5, label='Jooniseis')

x=np.arange(-9,-7,1)
y=7*(x+8)**2+1
plt.plot(x,y,color='r',linestyle=':', marker='h',markersize=5, label='Jooniseis')
x=np.arange(8,10,1)
y=7*(x-8)**2+1
plt.plot(x,y,color='r',linestyle=':', marker='h',markersize=5, label='Jooniseis')

x=np.arange(-8,0,1)
y=1/49*(x+1)**2
plt.plot(x,y,color='r',linestyle=':', marker='h',markersize=5, label='Jooniseis')
x=np.arange(1,9,1)
y=1/49*(x-1)**2
plt.plot(x,y,color='r',linestyle=':', marker='h',markersize=5, label='Jooniseis')

x=np.arange(-8,0,1)
y=-4/49*(x+1)**2
plt.plot(x,y,color='r',linestyle=':', marker='h',markersize=5, label='Jooniseis')
x=np.arange(1,9,1)
y=-4/49*(x-1)**2
plt.plot(x,y,color='r',linestyle=':', marker='h',markersize=5, label='Jooniseis')

x=np.arange(-8,-1,1)
y=1/3*(x+5)**2-7
plt.plot(x,y,color='r',linestyle=':', marker='h',markersize=5, label='Jooniseis')
x=np.arange(2,9,1)
y=1/3*(x-5)**2-7
plt.plot(x,y,color='r',linestyle=':', marker='h',markersize=5, label='Jooniseis')

x=np.arange(-2,0,1)
y=-2*(x+1)**2-2
plt.plot(x,y,color='r',linestyle=':', marker='h',markersize=5, label='Jooniseis')
x=np.arange(1,3,1)
y=-2*(x-1)**2-2
plt.plot(x,y,color='r',linestyle=':', marker='h',markersize=5, label='Jooniseis')

x=np.arange(-1,2,1)
y=-4*x**2+2
plt.plot(x,y,color='k',linestyle=':', marker='h',markersize=5, label='Jooniseis')
x=np.arange(-1,2,1)
y=4*x**2-6
plt.plot(x,y,color='k',linestyle=':', marker='h',markersize=5, label='Jooniseis')

x=np.arange(-2,1,1)
y=-1.5*x+2
plt.plot(x,y,color='k',linestyle=':', marker='h',markersize=5, label='Jooniseis')
x=np.arange(0,3,1)
y=1.5*x+2
plt.plot(x,y,color='k',linestyle=':', marker='h',markersize=5, label='Jooniseis')

plt.figure(facecolor='lightblue')
plt.title("Liblikas")
plt.xlabel("x telg")
plt.ylabel("y telg")
plt.grid(True)
plt.show()
