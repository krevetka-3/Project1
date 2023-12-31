# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uErp6TQyrTM0W3ucfbW3LRN0TH2jnoKq
"""

from logging import getLogRecordFactory
import math
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')


class Atom:
    def __init__(self,name, Z, A):
        '''
        Инициализация основных значений.
         name: Условное обозначение элемента. Type is string.
         Z: Номер атома . Type is int.
         A: Массовое число атома. Type is int.
        '''
        self.name = name
        self.Z = Z
        self.A = A
        self.G = None

        '''
        Расчет удельной энергии связи
        '''

    def binding_energy(self):

        a1 = 15.7
        a2 = 17.8
        a3 = 0.71
        a4 = 23.7
        a5 = 34.0
        neutro = self.A - self.Z
        if (self.Z % 2 == 0 and neutro % 2 == 0):
          self.G = (a1*self.A - a2*self.A**(2/3) - a3*(self.Z**2)/(self.A**(1/3)) - a4*(self.A - 2*self.Z)**2/self.A + a5*self.A**(-3/4))/self.A
        elif (self.A % 2 != 0):
          self.G = (a1*self.A - a2*self.A**(2/3) - a3*(self.Z**2)/(self.A**(1/3)) - a4*(self.A - 2*self.Z)**2/self.A)/self.A
        elif (self.Z % 2 != 0 and neutro % 2 != 0):
          self.G = (a1*self.A - a2*self.A**(2/3) - a3*(self.Z**2)/(self.A**(1/3)) - a4*(self.A - 2*self.Z)**2/self.A - a5*self.A**(-3/4))/self.A
        return self.G

        '''
        Расчет массы атома
        '''

    def atom_mass(self):

        mass = self.A * 1.660539040e-27
        print(f"The mass of the atom is {self.name}: {mass} kg")
        return mass

        '''
        Расчет радиуса атома
        '''

    def atom_radius(self):

        r0 = 1.2
        R = r0 * self.A**(1/3)
        return R

        '''
        Проверка на устойчивость к бета-распаду
        '''

    def stability_beta_decay(self):

        neutro = self.A - self.Z
        if (neutro > self.Z):
          print(f"The atom {self.name} is prone to beta minus decay")
        elif (neutro < self.Z):
          print(f"The atom {self.name} is prone to beta plus decay")
        elif (neutro == self.Z):
          print(f"The atom {self.name} is stable")

          '''
        Проверка на возможность деления на осколки

        '''

    def fragments(self):

        if ( self.Z**(2)/self.A > 17):
          print(f"The atom {self.name} can split into two identical even-even fragments")
        else:
          print(f"The atom {self.name} cant split into two identical even-even fragments")


'''
Расчет параметров атомов из заданного списка
'''
for i in range(0,11):
  mass = atoms[i].atom_mass()
  stability = atoms[i].stability_beta_decay()
  frags = atoms[i].fragments()
  print(f"Radius of the atom is {atoms[i].atom_radius()} angstroms")
  print(f"Binding energy of atom {atoms[i].name}: {atoms[i].binding_energy()} MeV")


U = Atom('U-238',92,238)
Pu239 = Atom('Pu-239',94,239)
Cf = Atom('Cf-252',98,252)
Pu238 = Atom('Pu-238',94,238)
Te = Atom('Te-135',52,135)
Ni = Atom('Ni-60',28,60)
O = Atom('O-16',8,16)
N = Atom('N-15',7,15)
P = Atom('P-29',15,29)
Si = Atom('Si-29',14,29)
Cr = Atom('Cr-52',24,52)

atoms = [Cf,Pu239,Pu238,U,Te,Ni,Cr,P,Si,O,N]

'''
Построение графиков для заданного набора атомов
'''
grf = list()
for i in range(0,11):
   grf.append(atoms[i].atom_radius())

plt.figure(figsize=[10, 5])
plt.plot([7,8,14,15,24,28,52,92,94,94,98], grf, linewidth=2)
plt.grid(True, color='#DDDDDD', linestyle='--', which='both')
plt.xlabel('Z')
plt.ylabel('Radius, Ангстрем')
plt.title('Зависимость радиуса атома от Z')
plt.xlim([0, 110])
plt.show()