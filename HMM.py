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
            par_ball.append(gg)
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
        path_1 = []
        with open('HMM.txt') as f:
            for path in f:
                path_1.append(path)
            vase_1_1 =path_1[0][2]+ path_1[0][3] + path_1[0][4]
            vase_1_2 =path_1[0][9]+ path_1[0][10] + path_1[0][11]
            vase_1_3 =path_1[0][16]+ path_1[0][17] + path_1[0][18]
            vase_2_1 =path_1[3][2]+ path_1[3][3] + path_1[3][4]
            vase_2_2 =path_1[3][9]+ path_1[3][10] + path_1[3][11]
            vase_2_3 =path_1[3][16]+ path_1[3][17] + path_1[3][18]
            vase_3_1 =path_1[6][2]+ path_1[6][3] + path_1[6][4]
            vase_3_2 =path_1[6][9]+ path_1[6][10] + path_1[6][11]
            vase_3_3 =path_1[6][16]+ path_1[6][17] + path_1[6][18]
            staypar_1 = path_1[1][0] + path_1[1][1] + path_1[1][2]
            staypar_2 = path_1[4][0] + path_1[4][1] + path_1[4][2]
            staypar_3 = path_1[7][0] + path_1[7][1] + path_1[7][2]
            self.r1_1par = int(vase_1_1[0])/10
            self.b1_1par = int(vase_1_1[1])/10
            self.y1_1par = int(vase_1_1[2])/10
            self.r1_2par = int(vase_1_2[0])/10
            self.b1_2par = int(vase_1_2[1])/10
            self.y1_2par = int(vase_1_2[2])/10
            self.r1_3par = int(vase_1_3[0])/10
            self.b1_3par = int(vase_1_3[1])/10
            self.y1_3par = int(vase_1_3[2])/10
            self.r2_1par = int(vase_2_1[0])/10
            self.b2_1par = int(vase_2_1[1])/10
            self.y2_1par = int(vase_2_1[2])/10
            self.r2_2par = int(vase_2_2[0])/10
            self.b2_2par = int(vase_2_2[1])/10
            self.y2_2par = int(vase_2_2[2])/10
            self.r2_3par = int(vase_2_3[0])/10
            self.b2_3par = int(vase_2_3[1])/10
            self.y2_3par = int(vase_2_3[2])/10
            self.r3_1par = int(vase_3_1[0])/10
            self.b3_1par = int(vase_3_1[1])/10
            self.y3_1par = int(vase_3_1[2])/10
            self.r3_2par = int(vase_3_2[0])/10
            self.b3_2par = int(vase_3_2[1])/10
            self.y3_2par = int(vase_3_2[2])/10
            self.r3_3par = int(vase_3_3[0])/10
            self.b3_3par = int(vase_3_3[1])/10
            self.y3_3par = int(vase_3_3[2])/10
            self.staypar1_1 = int(staypar_1[0])/10
            self.staypar1_2 = int(staypar_1[1])/10
            self.staypar1_3 = int(staypar_1[2])/10
            self.staypar2_1 = int(staypar_2[0])/10
            self.staypar2_2 = int(staypar_2[1])/10
            self.staypar2_3 = int(staypar_2[2])/10
            self.staypar3_1 = int(staypar_3[0])/10
            self.staypar3_2 = int(staypar_3[1])/10
            self.staypar3_3 = int(staypar_3[2])/10
    def calc(self):
        A1 = [[self.staypar1_1,1 - self.staypar1_1],
              [self.staypar1_2,1 - self.staypar1_2],
              [self.staypar1_3,1 - self.staypar1_3]]
        A2 = [[self.staypar2_1,1 - self.staypar2_1],
              [self.staypar2_2,1 - self.staypar2_2],
              [self.staypar2_3,1 - self.staypar2_3]]
        A3 = [[self.staypar3_1,1 - self.staypar3_1],
              [self.staypar3_2,1 - self.staypar3_2],
              [self.staypar3_3,1 - self.staypar3_3]]
        B1 = [[{'R':self.r1_1par,'B':self.b1_1par,'Y':self.y1_1par}],
              [{'R':self.r1_2par,'B':self.b1_2par,'Y':self.y1_2par}],
              [{'R':self.r1_3par,'B':self.b1_3par,'Y':self.y1_3par}]]
        B2 = [[{'R':self.r2_1par,'B':self.b2_1par,'Y':self.y2_1par}],
              [{'R':self.r2_2par,'B':self.b2_2par,'Y':self.y2_2par}],
              [{'R':self.r2_3par,'B':self.b2_3par,'Y':self.y2_3par}]]
        B3 = [[{'R':self.r3_1par,'B':self.b3_1par,'Y':self.y3_1par}],
              [{'R':self.r3_2par,'B':self.b3_2par,'Y':self.y3_2par}],
              [{'R':self.r3_3par,'B':self.b3_3par,'Y':self.y3_3par}]]
        row = len(pattern) - 2
        col = len(pattern)-1                 #要素数
        alpha = [[0 for s in range(row)] for t in range(col)]
        calcspace = [0,0]
        alpha[0][0] = B1[0][0][pattern[0]]
        for i in range(1,row):
            alpha[0][i] = alpha[0][i-1] * A1[0][0] * B1[0][0][pattern[i]]
        for j in range(1,col):
            alpha[j][0] = alpha[j-1][0] * A1[j-1][1] * B1[j][0][pattern[j]]
        for i in range(1,row):
            for j in range(1,col):
                calcspace[0] = alpha[j-1][i] * A1[j-1][1] * B1[j][0][pattern[j+1]]
                calcspace[1] = alpha[j][i-1] * A1[j][0] * B1[j][0][pattern[j+1]]
                alpha[j][i] = sum(calcspace)
        result1 = alpha[j][i] * A1[2][1]
        print(result1*100)
        alpha = [[0 for s in range(row)] for t in range(col)]
        calcspace = [0,0]
        alpha[0][0] = B2[0][0][pattern[0]]
        for i in range(1,row):
            alpha[0][i] = alpha[0][i-1] * A2[0][0] * B2[0][0][pattern[i]]
        for j in range(1,col):
            alpha[j][0] = alpha[j-1][0] * A2[j-1][1] * B2[j][0][pattern[j]]
        for i in range(1,row):
            for j in range(1,col):
                calcspace[0] = alpha[j-1][i] * A2[j-1][1] * B2[j][0][pattern[j+1]]
                calcspace[1] = alpha[j][i-1] * A2[j][0] * B2[j][0][pattern[j+1]]
                alpha[j][i] = sum(calcspace)
        result2 = alpha[j][i] * A2[2][1]
        print(result2 *100)
        alpha = [[0 for s in range(row)] for t in range(col)]
        calcspace = [0,0]
        alpha[0][0] = B3[0][0][pattern[0]]
        for i in range(1,row):
            alpha[0][i] = alpha[0][i-1] * A3[0][0] * B3[0][0][pattern[i]]
        for j in range(1,col):
            alpha[j][0] = alpha[j-1][0] * A3[j-1][1] * B3[j][0][pattern[j]]
        for i in range(1,row):
            for j in range(1,col):
                calcspace[0] = alpha[j-1][i] * A3[j-1][1] * B3[j][0][pattern[j+1]]
                calcspace[1] = alpha[j][i-1] * A3[j][0] * B3[j][0][pattern[j+1]]
                alpha[j][i] = sum(calcspace)
        result3 = alpha[j][i] * A3[2][1]
        print(result3 * 100)
vase_A = [10]
vase_B = [10]

vase_C = [10]
h = HMM(vase_A,vase_B,vase_C)
vase_all,par_Ball = h.Vase()
ball = []
s_par = []
select_ball,par = h.Select(vase_all[0])
select_ball,par = h.Select(vase_all[1])
select_ball,par = h.Select(vase_all[2])
line2 = []
h.read()
pattern = ['B','B','R','Y']
h.calc()
