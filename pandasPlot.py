import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

dataFrame = pd.read_excel("EquipoJonathan-datos.xlsx")

dtCM = pd.DataFrame(dataFrame,columns= ['Condición Médica'])

y = dtCM['Condición Médica'].value_counts()
y2 = list(y.items())
y3 = np.array(y2)
y4 = y3[::-1]

ax = plt.subplot(111)
plt.bar(y4[:,0], y4[:,1], color ='tab:green')

plt.xlabel('Condiciones')
plt.ylabel('Ocurrencias')
plt.title('Condciones medicas x Ocurrencias')

labels = ax.get_xticklabels()
ax.set_ylim(ymin=0)
plt.setp(labels, rotation=40, horizontalalignment='right')
plt.show()
