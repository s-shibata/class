#---------------------------------------------------
#Name : test7.py
#Author : s.shibata
#Created : 2017 / 07 / 21
#Last Date : 2017 / 07 / 24
#Note : with y.Ichimura & k.Maeda
#---------------------------------------------------

import numpy as np
import random
class HMM:
    def __init__(self,Vase1,Vase2,Vase3):
        self.vase1 = Vase1
        self.vase2 = Vase2
        self.vase3 = Vase3
    def Vase(self):
        d = []
        #g = []
        f = []
        #壺の数
        j = 3
        R = ['r']
        B = ['b']
        Y = ['y']
        for i in range(j):
            r = random.randint(1,8)
            b = random.randint(1,10-r-1)
            y = 10 - (r+b)
            g = (R * r) + (B * b) + (Y * y)
            gg = str(r) + str (b) + str(y)
            d.append(g)
            #print(gg)
            f.append(gg)
            #f.append()
        print(f)
        print(d)
        #self.vase1 = ["r","r","r","r","r","r","b","b","b","y"]
        #self.vase2 = ["b","b","b","b","b","b","y","y","y","r"]
        #self.vase3 = ["y","y","y","y","y","y","r","r","r","b"]
        return self.vase1,self.vase2,self.vase3
    def Select(self,select_ball):
        x = random.randint(3,7)
        v = random.choice(select_ball)
        b = 0
        ball.append(v)
        s_par.append(x)
        while (b == 0):
            a = random.randint(1,10)
            if a <= x:
                n = random.choice(select_ball)
                ball.append(n)
            else:
                b = 1
        return s_par,ball
    def write(self,ball_sum,prob):
        #print(prob)
        with open("HMM.txt","w") as f:
            f.write(str(ball_sum[0]))
            f.write(str(ball_sum[1]))
            f.write(str(ball_sum[2]))
            f.write("\n")
            f.write(str(prob))
            f.write("\n")
    def add(self,ball_sum,prob):
        with open("HMM.txt","a") as f:
            f.write(str(ball_sum[0]))
            f.write(str(ball_sum[1]))
            f.write(str(ball_sum[2]))
            f.write("\n")
            f.write(str(prob))
            f.write("\n")
    def read(self):
        f = open('HMM.txt')
        line = f.readline()
        f.close()
        #xx = list(line)
        #print(xx)
        for line1 in line:
            line2.append(line1)
            #ex2 = list(map(int,line2[0:-1]))
        print(line2)
        #a = 1
        #print(int(ex2[0]) + a)

    def calc(self):
        r1 = 0.6
        b1 = 0.4
        y1 = 0.1
        r2 = 0.4
        b2 = 0.1
        y2 = 0.6
        r3 = 0.1
        b3 = 0.6
        y3 = 0.4

vase_A = [10]
vase_B = [10]
vase_C = [10]
h = HMM(vase_A,vase_B,vase_C)
vase_all = h.Vase()
ball = []
s_par = []
select_ball,par = h.Select(vase_all[0])
select_ball,par = h.Select(vase_all[1])
select_ball,par = h.Select(vase_all[2])
#h.write(select_ball,par)
#h.add(select_ball,par)
#line2 = []
#h.read()

#print(select_ball)
#print(par)
