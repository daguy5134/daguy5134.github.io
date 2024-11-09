import numpy as np
print()
import matplotlib.pyplot as plt

x = np.array([1979, 1989, 1999, 2009, 2019])
y = np.array([9, 21, 41, 80, 134])

font1 = {'family':'serif','color':'blue','size':15}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Pays avec des lois de protections aux données", fontdict = font1)
plt.ylabel("Nombre de Pays", fontdict = font2)
plt.xlabel("Temps", fontdict = font2)

plt.plot(x, y)
plt.show()
