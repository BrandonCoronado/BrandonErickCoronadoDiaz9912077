#!/usr/bin/env python
# coding: utf-8

# In[6]:


#PRACTICA 2 INFORMATICA BRANDON ERICK CORONADO DIAZ 9912077 TAREA 2 - LAB 111


# In[4]:


x = float(input("introduce el tiempo que se puede invertir en segundos\n "))
z = float(input("introduce el tiempo en realizar la tarea en segundos\n "))
z_en_minutos = z // 60
z_minutos_resto = z % 60
z_en_horas = z_en_minutos // 60
z_horas_resto = z_en_minutos % 60
print("Tiempo que se puede invertir: ", z_en_horas, "h,",z_horas_resto,"m",z_minutos_resto,"s")
x_en_minutos = x // 60
x_minutos_resto = x % 60
x_en_horas = x_en_minutos // 60
x_horas_resto = x_en_minutos % 60
print("Tiempo para realizar la tarea: ", x_en_horas, "h,",x_horas_resto,"m",x_minutos_resto,"s")
x = float(x)
z = float(z)
if x >= z:
    print("se puede finalizar la tarea")
else:
    print("no se puede finalizar la tarea")


# In[4]:


a = float(input("introduce el coeficiente de la variable cuadratica\n "))
b = float(input("introduce el coeficiente de la variable lineal\n "))
c = float(input("introduce el termino independiente\n "))
D = b**2 - 4*a*c
D = float(D)
if D > 0:
    print("Son raices reales y diferentes")
if D == 0:
    print("Son raices reales e iguales")
if D < 0:
    print("son raices imaginarias (complejas)")


# In[5]:


a = float(input("introdusca un valor uno\n"))
b = float(input("introducir un valor dos\n"))
c = float(input("introducir un valor tres\n"))
a_en_minutos = a // 60
a_minutos_resto = a % 60
a_en_horas = a_en_minutos // 60
a_horas_resto = a_en_minutos % 60
b_en_minutos = b // 60
b_minutos_resto = b % 60
b_en_horas = b_en_minutos // 60
b_horas_resto = b_en_minutos % 60
c_en_minutos = c // 60
c_minutos_resto = c % 60
c_en_horas = c_en_minutos // 60
c_horas_resto = c_en_minutos % 60
a = float(a)
b = float(b)
c = float(c)
x = a_minutos_resto + 1
y = b_minutos_resto + 1
z = c_minutos_resto + 1
print("Tiempo uno introducido\n ", a_en_horas, "h,",a_horas_resto,"m",a_minutos_resto,"s")
print("Tiempo dos introducido\n ", b_en_horas, "h,",b_horas_resto,"m",b_minutos_resto,"s")
print("Tiempo tres introducido\n ", c_en_horas, "h,",c_horas_resto,"m",c_minutos_resto,"s")
print("Tiempos introducidos sumandoles un segundo")
print("Tiempo uno sumandole un segundo\n ", a_en_horas, "h,",a_horas_resto,"m",x,"s")
print("Tiempo dos sumandole un segundo\n ", b_en_horas, "h,",b_horas_resto,"m",y,"s")
print("Tiempo tres sumandole un segundo\n ", c_en_horas, "h,",c_horas_resto,"m",z,"s")

