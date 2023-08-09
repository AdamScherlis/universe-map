#!/usr/bin/python

import csv
from math import *

METER = 34.64099
GRAM = 4.8127545
UNITLENGTH = 0.1 #inches
HORIZON = 60.855228 

fi = open('lines.csv', 'rb')
rdr = csv.reader(fi)

for row in rdr:
  if not row[0].startswith('//'):
    lin = row[0]
    [x0,y0,mx,my,labx] = map(float,row[1:6])
    clr = row[6]
    ends = row[7:9]
    
    if mx!=0:
      m = my/mx
      b = y0-m*x0
      tilt = atan(m)*360/(2*pi)

      xnd = []
      ynd = []
      for end in ends:
        if end == 'LEFT':
          ynd.append(b/(1+m))
          xnd.append(-b/(1+m))
        elif end == 'RIGHT':
          ynd.append(b/(1-m))
          xnd.append(b/(1-m))
        elif end == 'TOP':
          ytop = HORIZON
          ynd.append(ytop) 
          xnd.append((ytop-b)/m)
        else:
          raise Exception('invalid endpoint "%s" for line "%s"' % (end,lin)) # ooh fancy

      iL = int(xnd[1]<xnd[0]) # somewhat immoral
      iR = 1-iL
      [xL,yL] = [xnd[iL],ynd[iL]]
      [xR,yR] = [xnd[iR],ynd[iR]]
      dx = xR-xL
      
      laby = m*labx+b-1.3 # adjust y offset to taste
    else:
      xL = x0
      yL = abs(x0)
      dx = HORIZON-yL
      tilt = 90
      laby = labx
      labx = x0+.2


    print('\put(%3.4f,%3.4f){\\textcolor{%s}{\line(%d,%d){%s}}}' % (xL,yL,clr,mx,my,dx))
    print('\put(%3.4f,%3.4f){\\textcolor{%s}{\\begin{turn}{%s}\large %s\end{turn}}}' \
      % (labx,laby,clr,tilt,lin))

fi = open('imgs.csv', 'rb')
rdr = csv.reader(fi)

for row in rdr:
  if not row[0].startswith('//'):
    img = row[0]
    [w,h,x1,x1v,x2,x2v,y1,y1v,y2,y2v] = map(float,row[1:11])
    
    scalex = (x2v-x1v)/(x2-x1)
    scaley = (y2v-y1v)/(y2-y1) #inverted y axis watch out
    leftv = x1v-scalex*x1
    bottomv = y1v-scaley*y1+scaley*h
    left = leftv+GRAM
    bottom = bottomv+METER
    width = w*scalex*UNITLENGTH
    height = -h*scaley*UNITLENGTH #nb minus sign

    print('\put(%3.4f,%3.4f){\hbox{\includegraphics[width=%3.4fin,height=%3.4fin]{img/%s}}}' \
      % (left,bottom,width,height,img))

fi = open('pts.csv', 'rb')
rdr = csv.reader(fi)

for row in rdr:
  if not row[0].startswith('//'):
    pt = row[0]
    [mass,rad] = [float(row[1])+GRAM,float(row[2])+METER]
    
    if 'N' in row: 
      print('\put(%3.4f,%3.4f){%s}' % (mass-.5,rad+.9,pt))
      print('\put(%3.4f,%3.4f){$\\bullet$}' % (mass-.35,rad-.35))
    elif 'S' in row:
      print('\put(%3.4f,%3.4f){%s}' % (mass-.5,rad-1.9,pt))
      print('\put(%3.4f,%3.4f){$\\bullet$}' % (mass-.35,rad-.35))
    elif 'NW' in row:
      print('\put(%3.4f,%3.4f){%s}' % (mass-3.5,rad+.9,pt))
      print('\put(%3.4f,%3.4f){$\\bullet$}' % (mass-.35,rad-.35))
    else: 
      print('\put(%3.4f,%3.4f){$\\bullet$ %s}' % (mass-.35,rad-.35,pt))


#for i in range(1,7):
#    print('\put(%d,%d){\line(1,0){%d}}' % (-10*i,10*i,20*i))
#
#for i in range(6):
#    print('\put(%d,%d){\line(0,1){%d}}' % (-10*i,10*i,60-10*i))
#
#for i in range(1,6):
#    print('\put(%d,%d){\line(0,1){%d}}' % (10*i,10*i,60-10*i))
