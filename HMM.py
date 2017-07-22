#---------------------------------------------------
#Name : test7.py
#Author : s.shibata
#Created : 2017 / 07 / 21
#Last Date : 2017 / 07 / 24
#Note : with y.Ichimura & k.Maeda
#---------------------------------------------------

import numpy as np
import random
import csv
class HMM:
    def __init__(self,Vase1,Vase2,Vase3):
        self.vase1 = Vase1
        self.vase2 = Vase2
        self.vase3 = Vase3
    def Vase(self):
        par_ball = []
        #g = []
        enu_ball = []
        #壺の数
        j = 3
        R = ['r']
        B = ['b']
        Y = ['y']
        for i in range(j):
            self.r = random.randint(1 , 8)
            self.b = random.randint(1 , 10 - self.r - 1)
            self.y = 10 - ( self.r + self.b )
            g = (R * self.r) + (B * self.b) + (Y * self.y)
            gg = str(self.r) + str (self.b) + str(self.y)
            enu_ball.append(g)
            #print(gg)
            par_ball.append(gg)
        #print(f[0])
        #print(d[0])
        #self.vase1 = ["r","r","r","r","r","r","b","b","b","y"]
        #self.vase2 = ["b","b","b","b","b","b","y","y","y","r"]
        #self.vase3 = ["y","y","y","y","y","y","r","r","r","b"]
        return enu_ball,par_ball
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
        return ball,s_par
    def write(self,par_Ball,ball_sum,prob):
        #print(prob)


        with open("HMM.txt","w") as f:
            f.write(str(par_Ball))
            f.write("\n")
            f.write(str(ball_sum[0]))
            f.write(str(ball_sum[1]))
            f.write(str(ball_sum[2]))
            f.write("\n")
            f.write(str(prob))
            f.write("\n")
    def add(self,par_Ball,ball_sum,prob):
        with open("HMM.txt","a") as f:
            f.write(str(par_Ball))
            f.write("\n")
            f.write(str(ball_sum[0]))
            f.write(str(ball_sum[1]))
            f.write(str(ball_sum[2]))
            f.write("\n")
            f.write(str(prob))
            f.write("\n")
    def read(self):

        with open('HMM.txt') as f:
            #reader = csv.reader(f,delimiter = '\n')
            line = f.readline()
            for line1 in line:
                line2.append(line1)
                #self.ex2 = list(map(int,line2[0:-1]))
            print(line2)
        #return ex2

        #a = 1
        #print(int(ex2[0]) + a)

    #RBBのとき
    def calc(self):
        x = self.r + int(self.ex2[0])
        print(self.r,x)


vase_A = [10]
vase_B = [10]
vase_C = [10]
h = HMM(vase_A,vase_B,vase_C)
vase_all,par_Ball = h.Vase()
#print(par_Ball)
#print(vase_all)

ball = []
s_par = []
select_ball,par = h.Select(vase_all[0])
select_ball,par = h.Select(vase_all[1])
select_ball,par = h.Select(vase_all[2])
#print(par)
#print(select_ball)
#h.write(par_Ball,par,select_ball)
#h.add(par_Ball,par,select_ball)
line2 = []

h.read()
#h.calc()
#print(select_ball)
#print(par)
