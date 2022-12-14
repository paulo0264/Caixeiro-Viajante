import numpy as np
import math as m 
import matplotlib.pyplot as plt #coordenadas dos locais em que o Caixeiro deverá passar
x = [5,5,7,8,8]
y = [10,6,2,2,3]
n = len(x) #numero de pontos em que o Caixeiro deverá passar

#Em seguida são calculadas as distâncias
distOriginal = np.zeros((n,n)) # reservando memória para a distancia de um ponto a todos os outros
a = 1000*np.identity(n,int) # criando uma matrix identidade com valor alto, para que o vizinho mais próximo não seja o proprio ponto
for i in range(0,n):
    for j in range(0,n):
        distOriginal[i,j] = a[i,j]+m.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2) #calculo da distância euclidiana de um ponto a todos os outros pontos
        #neste cenário estamos considerando a distância euclidiana, porém poderiamos dar pesos as distâncias que representariam a distância ao 
        #percorrida por uma estrada utilizada.
rota = np.zeros((n,n)) # resernvado memória para a rota que será utilizada
distTotal = np.zeros((1,n)) # reservando memória para a distância percorrida

#criando uma matriz de rotas, desta forma é possível calcular todas elas para todos os pontos de partida e definir qual a rota mais curta.
for i in range(0,n):
    dist = distOriginal 
    distAtual = dist[i,0:n] #distâncias do ponto x
    rota[i,0] = i #ponto xda rota
    minDist = min(distAtual) #ponto mais próximo do ponto
    pos = distAtual.tolist().index(minDist) #numero do ponto mais próximo
    rota[i,1] = pos #segundo ponto da rota
    distTotal[0,i] = distTotal[0,i] + minDist #distancia percorrida
    dist[0:n,i] = 1000 #atribuindo valor grande para ponto já utilizado, para que não volte a ser utilizado

    count = 2    #processo para seleção dos próximos pontos seguinte a lógica anterior
    while (count < n):
        aux = pos
        distAtual = dist[aux,0:n]
        minDist = min(distAtual)
        pos = distAtual.tolist().index(minDist)
        rota[i,count] = pos
        distTotal[0,i] = distTotal[0,i]+minDist
        dist[0:n,aux] = 1000
        count = count+1     
    else:
        distTotal[0,i] = distTotal[0,i]+distOriginal[i,int(rota[i,-1])] #distancia do ultimo ponto de volta ao primeiro

#seleção do melhor ponto de partida
minDistTotal = min(distTotal[0,0:n]) 
posInicialTotal = distTotal[0,0:n].tolist().index(minDistTotal) 
#plot para melhor rota
melhorRota = rota[posInicialTotal,0:n]
xMelhor = np.zeros((1,n+1))
yMelhor = np.zeros((1,n+1))

for i in range(0,n):
    xMelhor[0,i] = x[int(melhorRota[i])]
    yMelhor[0,i] = y[int(melhorRota[i])]
xMelhor[0,n] = xMelhor[0,0]
yMelhor[0,n] = yMelhor[0,0]
x2 = xMelhor[0,0:n+1]
y2 = yMelhor[0,0:n+1]       
plt.plot(x,y, 'ro')
plt.axis([-1, 11, 0, 11])
plt.plot(x2,y2,'b-')
plt.show()