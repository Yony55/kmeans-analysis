import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

dataFrame = pd.read_excel("EquipoJonathan-datos.xlsx")

dtT = pd.DataFrame(dataFrame,columns= ['Tipo Empleado'])
dtS = pd.DataFrame(dataFrame,columns= ['Salario Diario'])
dtT['Tipo Empleado']	= dtT['Tipo Empleado'].replace({"Directo": 0, "Indirecto": 1, "Especializado": 2})
dt2 = pd.DataFrame(dataFrame,columns= ['Condición Médica','Edad'])
dt2['Condición Médica'] = dt2['Condición Médica'].replace({"Diabetes": 0, "Diabetes e Hipertensión": 1, "Otros Medicos": 2,
                                                           "Edad": 3, "Lupus": 4, "Embarazo": 5, "Hipertensión": 6})
dt3 = pd.DataFrame(dataFrame,columns= ['Antig','Salario Diario'])

wcss = []
for i in range(1, 10):
  kmeans = KMeans(n_clusters = i, max_iter = 300)
  kmeans.fit(dtT)
  wcss.append(kmeans.inertia_)

wcss2 = []
for i in range(1, 10):
  kmeans = KMeans(n_clusters = i, max_iter = 300)
  kmeans.fit(dt2)
  wcss2.append(kmeans.inertia_)

wcss3 = []
for i in range(1, 10):
  kmeans = KMeans(n_clusters = i, max_iter = 300)
  kmeans.fit(dt3)
  wcss3.append(kmeans.inertia_)
  
plt.plot(range(1, 10), wcss)
plt.xlabel("Clusters")
plt.ylabel("WCSS")
plt.title("Codo de Jambú: Tipo Empleado vs Salario Diario")
plt.show()
plt.plot(range(1, 10), wcss2)
plt.xlabel("Clusters")
plt.ylabel("WCSS")
plt.title("Codo de Jambú: Condción Médica vs Edad")
plt.show()
plt.plot(range(1, 10), wcss3)
plt.xlabel("Clusters")
plt.ylabel("WCSS")
plt.title("Codo de Jambú: Antiguedad vs Salario Diario")
plt.show()

kmeans= KMeans(n_clusters=3, max_iter=300).fit(dtT)
centroids = kmeans.cluster_centers_

plt.scatter (dtT['Tipo Empleado'], dtS['Salario Diario'], c=kmeans.labels_.astype(float), s=50, alpha= 0.5)
plt.scatter(centroids[:,0], centroids[:,0], c='red', s=50)
plt.title("Tipo de Empleado vs Salario Diario")
plt.xlabel("Tipo de Empleado")
plt.ylabel("Salario Diario")
plt.show()
