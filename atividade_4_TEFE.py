import numpy as np
from math import sin
import math

def toy_MC1(iteracoes, valor_verdadeiro, desvio_padrao):
    numeros_gauss=valor_verdadeiro+np.random.randn(iteracoes)*desvio_padrao
    calc_func = [sin(i) for i in numeros_gauss]
    print("Exercicio 1 \n O desvio padrão amostral é: ",np.round(np.std(calc_func),3),
          "\n O valor médio da grandeza é: ",np.round(np.mean(calc_func),5),
          "\n O desvio padrão da media é: ",np.round(np.std(calc_func)/np.sqrt(iteracoes),5),"\n")
    return   

def toy_MC2(iteracoes, valor_verdadeiro): 
    sistematico = np.random.randn()*3
    numeros_gauss = valor_verdadeiro+np.random.randn(iteracoes)*28 + sistematico
    return np.mean(numeros_gauss)

def toy_MC3(iteracoes,desvio_p, tempo_verdadeiro): 
    tm = tempo_verdadeiro+np.random.randn(iteracoes)*desvio_p
    return np.mean(tm)

def toy_MC4(iteracoes,desvio_p, tempo_verdadeiro): 
    tm = tempo_verdadeiro+np.random.randn(iteracoes)*desvio_p
    am = 68/tm**2
    return np.mean(am)

##Exericicio 1
iteracoes = 10000
x_0 = math.radians(85)
sigma = math.radians(10)
toy_MC1(iteracoes,x_0,sigma)

#Exericicio 2
x_0 = 100
x = np.array([toy_MC2(50,x_0) for i in range(iteracoes)])
g = np.round(np.std(x),1)
maior_que_x_0 = (np.array(x) > x_0).sum()
menor_que_g = (np.abs(x-x_0)<g).sum()
print("Exercicio 2 \n Item a - Incerteza final(com 2 significativos) é: ",g,
          "\n Item b - Repetições maiores que o valor verdadeiro: ",maior_que_x_0,
          "\n Item c - Repetições xf (modulo de x -x_0) menores que a incerteza final: ",
          menor_que_g,"\n")

#Exericicio 3 
t_0 =   2.525
sigma = 0.15
a_0 = 68/(t_0)**2
af = np.array([68/(toy_MC3(287,sigma,t_0))**2 for i in range(iteracoes)])
ai =np.round(np.std(af),3)
maior_que_a_0 = (af > a_0).sum()
menor_que_ai = (np.abs(af-a_0)<ai).sum()
print("Exercicio 3\n Item a - Incerteza aceleração final(com 2 significativos) é: ",ai,
          "\n Item b - Repetições maiores que o valor verdadeiro: ",maior_que_a_0,
          "\n Item c - Repetições xf (modulo de x -x_0) menores que a incerteza final: ",
          menor_que_ai,"\n")

#Exericicio  4
t_0 =   2.525
sigma = 0.15
a_0 = 68/(t_0)**2
af = np.array([(toy_MC4(287,sigma,t_0)) for i in range(iteracoes)])
ai =np.round(np.std(af),3)
maior_que_a_0 = (af > a_0).sum()
menor_que_ai = (np.abs(af-a_0)<ai).sum()
print("Exercicio 4\n Item a - Incerteza aceleração final(com 2 significativos) é: ",ai,
          "\n Item b - Repetições maiores que o valor verdadeiro: ",maior_que_a_0,
          "\n Item c - Repetições xf (modulo de x -x_0) menores que a incerteza final: ",
          menor_que_ai,"\n")







 








