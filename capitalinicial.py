# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 12:50:43 2022

@author: manue
"""

c= float (input("ingrese un capital inicial:"))
t= float (input("ingrese una tasa de interes:"))
n= int(input ("ingrese un número entero de años:"))

print("Capital final:", (c*(1+t/100)**n), "pesos")
print("Cálculo de capital finalizado correctamente")
