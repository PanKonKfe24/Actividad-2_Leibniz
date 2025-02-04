"""
           Autor:
   Juan Pablo Buitrago Rios
   juanybrisagames@gmail.com
   Version 2.0 : 04/02/2025 01:40am

"""
import numpy as np #Importe para realizar calculos numérico
import matplotlib.pyplot as plt #Importe para realizar y visualizar gráficos

def leibniz_pi(n):
    """La serie de Leibniz para pi es:  pi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + repitiendo el patron sucesivamente)"""
    return 4 * sum((-1)**k / (2*k + 1) for k in range(n))  # Calcula la suma de la serie de Leibniz

#Inicializar variables
true_pi = np.pi #Valor de Pi
N_values = [10, 100, 1000, 10000] #Lista de valores de N
#Listas para almacenar los errores
errors_abs = [] #Error absoluto
errors_rel = [] #Error Relativo
errors_cua = [] #Error Cuadrático

#Iteramos sobre los N valores
for N in N_values:
    approx_pi = leibniz_pi(N) # Aproximamos Pi con el valor N en turno
    error_abs = abs(true_pi - approx_pi) #Calculamos el error absoluto
    error_rel = error_abs / true_pi #Calculamos error relativo
    error_cua = error_abs**2 #Calculamos error cuadrático
    #Agregamos los errores calculados a sus respectivas listas
    errors_abs.append(error_abs)
    errors_rel.append(error_rel)
    errors_cua.append(error_cua)
    #Mostramos los errores calculados sobre el valor N en turno
    print(f"N={N}: Error absoluto={error_abs}, Error relativo={error_rel},Error cuadratico={error_cua}")

plt.figure() #Crear figura
plt.plot(N_values, errors_abs, label='Error absoluto', marker='o') #Generamos la linea de tendencia del error absoluto
plt.plot(N_values, errors_rel, label='Error relativo', marker='s') #Generamos la linea de tendencia del error relativo
plt.plot(N_values, errors_cua, label='Error cuadratico', marker='^') #Generamos la linea de tendencia del error cuadrático
#Se establece una escala logarítmica en ambos ejes 
plt.xscale('log')
plt.yscale('log')
#Titulos 
plt.xlabel('N')
plt.ylabel('Error')
plt.legend() #Mostrar leyenda
plt.title('Errores en la aproximación de pi') #Título del gráfico
plt.show() #Mostrar Gráfico