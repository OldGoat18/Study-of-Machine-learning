
'''
这是一个感知机学习算法的简单模型，
对于直线两端的点进行分类，分别用-1，1表示，
并通过感知机预测这一直线
使用梯度下降法逼近函数
'''
# 数据获得
import random
fileObject = open('./point.txt', 'w')
for i in range(1, 100, 1):
    a = random.uniform(-100, 100)
    b = random.uniform(-100, 100)
    if (3*a+5*b-4) > 0:
        c = 1
    else:
        c = -1
    ipTable = [a, b, c]
    for ip in ipTable:
        fileObject.write(str(ip))
        if ip != c:
            fileObject.write(',')
    fileObject.write('\n')
fileObject.close()

# 数据读取
point = []
fileObject = open('./point.txt', 'r')
line = fileObject.readline()
while line:
    link = []
    line = line.split(',')
    for i in line:
        j = float(i)
        link.append(j)
    point.append(link)
    line = fileObject.readline()
# 函数为wx+b,其中w为1*2矩阵，x为2*1矩阵，初始设置均为0
# 学习率(下降梯度)为z(0<z<=1)
# 判断方式为没有错误点
w = [2, 10]
b = -2
z = 1
jud = 0
while jud < 99:
    jud = 0
    for i in point:
        while((w[0]*i[0]+w[1]*i[1] + b)*i[2]) < 0:
            '''
            学习的方法，不断改变w与b来趋近结果，
            这里是书上的w与b的学习函数
            但效果并不好(或者说很糟糕，根本无法正常学习，常常跑偏)
            仅仅当对于极大容错率(如样本极少，可以有多个结果)，
            且初始值即贴近结果的时候才可以勉强一用。
            '''
            w[0] = w[0] + z * i[2] * i[1]
            w[1] = w[1] + z * i[2] * i[1]
            b = b + z * i[2]
        if ((w[0]*i[0]+w[1]*i[1] + b)*i[2]) < 0:
            jud = jud + 1
print(w[1]/w[0], b)
