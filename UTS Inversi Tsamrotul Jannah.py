# -*- coding: utf-8 -*-
"""UTS Inversi 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CIQpIP0qIw--zT3oQfOlYdKePygTRxpW
"""

import numpy as np
import matplotlib.pyplot as plt

z = [30, 70, 180, 250, 300]
T = [25, 26.2, 29.7, 34.3, 35.5]
N = len(z)
#menentukkan nilai koefisien, T=az + b, jadi menentukan nilai a dan b
#nomor 1a
#Kernel Matrix
G = np.ones((N,3))
G[:,1] = z
for i in range (N):
    G[i,2] = z[i]**2

#kemudian dilakukan perhitungan inversi
GT = np.transpose(G)
GTGInv = np.linalg.inv(np.dot(GT,G))

#menampilkan nilai a dan b
m_est = np.dot(GTGInv,np.dot(GT,T))
print("nilai a :", m_est[1])
print("nilai b :", m_est[0])

#nomor 1b
#perhitungan missfit
#menghitung misfit
misfit = 0

for i in range(N):
    misfit = misfit + (T[i]-(m_est[1]*z[i] + m_est[0]))**2
print("misfit :", misfit)

#bagian c
#prediksi besar suhu
T1 = m_est[1]*(100) + m_est[0]
T2 = m_est[1]*(200) + m_est[0]
T3 = m_est[1]*(350) + m_est[0]

print("T pada kedalaman 100 : ", T1)
print("T pada kedalaman 200: ", T2)
print("T pada kedalaman 350: ", T3)