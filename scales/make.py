#!/usr/bin/python

import csv
from math import log10

udic = {
  'ev' : [1,0],
  'ev^2' : [2,0],
  'MeV' : [1,6],
  'gev' : [1,9],
  'inch' : [-1,-5.1096473],
  'nm' : [-1,9-6.7048135],
  'cm' : [-1,-4.7048135],
  'm' : [-1,-6.7048135],
  'km' : [-1,-9.7048135],
  'm^-2' : [2,-6.7048135],
  'km/s/Mpc': [1,-34.670985],
  'kg/m^3' : [4,3.9086226],
  'year' : [-1,-22.680738],
  's' : [-1,-15.181634],
  'hz' : [1,-15.181634],
  'Cal' : [1,22.417172],
  'J' : [1,18.79529],
  'g' : [1,32.748931],
  'amu' : [1,8.9691801],
  'bp' : [1,11.782093]
}

inv = {'inch'}

n = -33;
for pf in 'vwxyzafpnum kMGTPEZYXW':
  print('\draw (-3,%d) node[left]{%seV};' % (n,pf))
  n += 3

fi = open('scales.csv', 'rb')
rdr = csv.reader(fi)
off = -4 #haaaack
for row in rdr:
  if len(row)==1:
    off += 4
    print('\draw (%d+1,31) node[right]{%s};' % (off,row[0]))
  elif not row[0].startswith('//'):
    [name,val,unit] = row[:3]
    [b,a] = udic[unit] 
    lg = a+log10(float(val))/b
    if len(row)==4:
      val2 = row[3]
      lg2 = a+log10(float(val2))/b
      print('\draw (%d,%3.4f) -- (%d,%3.4f);' % (off,lg,off+1,lg))
      print('\draw (%d,%3.4f) -- (%d,%3.4f);' % (off,lg2,off+1,lg2))
      print('\draw (%f,%3.4f) -- (%f,%3.4f);' % (off+.5,lg,off+.5,lg2))
      print('\draw (%d,%3.4f) node[right]{%s};' % (off+1,(lg+lg2)/2.0,name))
    else:
      print('\draw (%d,%3.4f) -- (%d,%3.4f) node[right]{%s};' % (off,lg,off+1,lg,name))
