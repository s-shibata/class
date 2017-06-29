import glob
import csv
import numpy as np
import sys
import math
import matplotlib.pyplot as plt

def read(files):
    tem = []
    tem_info = []
    for path in files:
        ao = []
        ao_info = []
        with open(path,'r') as f:
            reader = csv.reader(f, delimiter = ' ')
            for p, row in enumerate(reader):
                if p < 3:
                    ex1 = list(row)
                    ao_info.append(ex1)
                else:
                    ex2 = list(map(float,row[0:-1]))
                    ao.append(ex2)
            tem.append(ao)
            tem_info.append(ao_info)
    return tem,tem_info

def Maching(data_tem,data_ano):
    Matrix = []
    Matrix_all = []
    #g = [[0 for s in range(len(data_tem))] for t in range(len(data_ano))]
    for i in range(len(data_tem)):
        for j in range(len(data_ano)):
            result = 0
            for k in range(15):
                re = (data_tem[i][k] - data_ano[j][k])**2
                result += re
            D = result**0.5
            Matrix.append(D)
    Matrix_arr = np.array(Matrix)
    Matrix_all = np.reshape(Matrix_arr,(len(data_tem),len(data_ano)))
    #print(Matrix_all)
    #exit()
    print(Matrix_all)
    return Matrix_all

def Calc(aa):

    row = len(aa[0])
    col = len(aa)
    g = [[0 for s in range(row)] for t in range(col)]
    g[0][0] = aa[0][0]
    for i in range(1,row):
        g[0][i] = g[0][i-1] + aa[0][i]
    for j in range(1,col):
        g[j][0] = g[j-1][0] + aa[j][0]
    for j in range(1,col):
        for i in range(1,row):
            calcg = []
            calcg.append(g[j-1][i] + aa[j][i])
            calcg.append(g[j-1][i-1] + 2 * aa[j][i])
            calcg.append(g[j][i-1] + aa[j][i])
            g[j][i] = min(calcg)
    return g[col-1][row-1]/float(col+row),g

def plotMat(mat, locus, save = None):
    x = np.arange(len(mat[0])+1)
    y = np.arange(len(mat)+1)
    X, Y = np.meshgrid(x, -y)
    plt.pcolor(X, Y, np.array(mat), cmap=plt.cm.binary)
    plt.colorbar()
    plt.plot(locus[0],locus[1])
    plt.xlim(0, len(mat[0]))
    plt.ylim(-len(mat),0)
    if save is None:
        plt.show()
    else:
        plt.savefig(save + ".png")

def plotRoute(mat):
    y = len(mat) - 1
    x = len(mat[0]) - 1
    locusX = [x + 0.5]
    locusY = [-y - 0.5]
    locus = []
    while x != 0 or y != 0:
        if x == 0:
            y -= 1
        elif y == 0:
            x -= 1
        else:
            #print(str(x) + ", " + str(y))
            num = np.argmin(np.array([mat[y - 1][x], mat[y - 1][x - 1], mat[y][x - 1]]))
            if num == 0:
                y -= 1
            elif num == 1:
                x -= 1
                y -= 1
            elif num == 2:
                x -= 1
        locusX.append(x + 0.5)
        locusY.append(-y - 0.5)
    locus.append(locusX)
    locus.append(locusY)
    """
    plt.plot(locusX,locusY)
    plt.xlim(0, len(mat[0]) - 1)
    plt.ylim(-len(mat) + 1)
    plt.show()
    """
    return locus

def main(arg):
    files_tem = glob.glob(arg[1] + '/*.txt')
    files_ano = glob.glob(arg[2] + '/*.txt')
    tmp,info = read(files_tem)
    ano,info_ano = read(files_ano)
    T = 0
    F = 0
    for path_tem,path_info in zip(tmp,info):
        G_G = []
        G_info_ano =[]
        for path_ano,path_info_ano in zip(ano,info_ano):
            D = Maching(path_tem,path_ano)
            G,G_A =  Calc(D)
            print(G)
            re = plotRoute(G_A)
            #plotMat(D,re)
            G_G.append(G)
            G_info_ano.append(path_info_ano[1])
        G_num =  np.argmin(G_G)

        if path_info[1] == G_info_ano[G_num]:
            T +=1
        else:
            print("{0}, {1}".format(path_info[1], G_info_ano[G_num]))
            F +=1
    #print("正答率",T,"%")

if __name__ == "__main__":
        main(sys.argv)
