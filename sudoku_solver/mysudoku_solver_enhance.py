#coding:utf-8
#python3.5
#Create:   2018-5-12
#Complete: 2018-5-12
import time
import copy
import numpy as np
from queue import LifoQueue, Queue

class Recorder:
    point = None        #进行猜测的点的坐标
    point_index = 0     #猜测候选列表使用的值的索引？什么意思呢？
    board = None        #回溯记录的9*9数组
    
class Sudo:
    def __init__(self, data):
        #数据初始化
        self.board = np.array([[0]*9]*9, dtype=object)
        self.new_point = Queue() #先进先出的新解坐标

        #后半部分需要的属性
        self.recorder = LifoQueue() #先进先出回溯器
        self.guess_times = 0        #猜测次数

        #九宫格基准列表
        self.base_point = [[0,0],[0,3],[0,6],
                           [3,0],[3,3],[3,6],
                           [6,0],[6,3],[6,6]]
        #整理数据
        #将81个元素的list转化为9*9的二维数组
        data = np.array(data).reshape(9,-1)
        for r in range(9):
            for c in range(9):
                #如果data[r,c]不为0,说明该结点填的是一个确定的数字
                if data[r,c] != 0:
                    self.board[r,c] = int(data[r,c])
                    #新点添加到列表中，以便遍历
                    #每新增一个确定的数字，则加入这个列队
                    #后续处理则从这个列队中取出数字
                    #排除所在行列和九宫格其他候选值
                    self.new_point.put((r,c))
                else:
                    self.board[r,c] = [i for i in range(1,10)]
    #剔除数字
    def cut_num(self, point):#这个point一定是已经确定的数字，然后从别的格中剔除重复的数字
        r, c = point
        val  = self.board[r,c]

        #行
        for i, item in enumerate(self.board[r]):
            if isinstance(item, list):
                #当这一格的列表中含有该候选值时，则剔除
                if item.count(val) != 0:
                    item.remove(val)
                    #判断移除后，是否剩下一个元素
                    if len(item) == 1:
                        #将新的已经确认的点加入队列中
                        self.new_point.put((r, i))
                        #赋值，使其为int类型
                        self.board[r,i] = item[0]
        #列
        for i, item in enumerate(self.board[:,c]):
            if isinstance(item, list):
                #当这一格的列表中含有该候选值时，则剔除
                if item.count(val) != 0:
                    item.remove(val)
                    #判断移除后，是否剩下一个元素
                    if len(item) == 1:
                        #将新的已经确认的点加入队列中
                        self.new_point.put((i,c))
                        #赋值，使其为int类型
                        self.board[i,c] = item[0]

        #所在九宫格(3x3的数组)
        b_r, b_c = map(lambda x:int(x/3)*3,point)
        for m_r, row in enumerate(self.board[b_r:b_r+3, b_c:b_c+3]):
            for m_c, item in enumerate(row):
                if isinstance(item, list):
                    #当这一格的列表中含有该候选值时，则剔除
                    if item.count(val):
                        item.remove(val)
                        #判断移除后，是否剩下一个元素
                        if len(item) == 1:
                            r = b_r + m_r
                            c = b_c + m_c
                            #将新的已经确认的点加入队列中
                            self.new_point.put((r,c))
                            #赋值，使其为int类型
                            self.board[r,c] = item[0]
    #剔除数字法解数独
    def solve_sudo(self):
        while not self.new_point.empty():
            point = self.new_point.get()  #先进先出
            self.cut_num(point)
    #-------------------------------------------------------------------------------------
    ######################### 下面为猜测法解数独 ##################################
    #得到有多少个确定的数字
    def get_num_count(self):
        return sum(map(lambda x: 1 if isinstance(x,int) else 0, self.board.reshape(1,-1)[0]))
    #检查数独盘有没有错误
    def check_board(self):
        #行
        for row in self.board:
            nums = []
            lists = []
            for item in row:
                (lists if isinstance(item, list) else nums).append(item)
            if len(set(nums)) != len(nums):
                return False #数字要不重复
            if len(list(filter(lambda x: len(x)==0, lists))):
                return False #候选列表不能为空集
        #列
        for c in range(9):
            nums = []
            lists = []
            col = self.board[:,c]
            for item in col:
                (lists if isinstance(item, list) else nums).append(item)
            if len(set(nums)) != len(nums):
                return False  #数字要不重复
            if len(list(filter(lambda x: len(x) == 0, lists))) != 0:
                return False  #候选列表不能为空集
        #九宫格
        for b_r, b_c in self.base_point:
            nums = []
            lists = []
            block = self.board[b_r:b_r+3, b_c:b_c+3].reshape(1,-1)[0]

            for item in block:
                (lists if isinstance(item, list) else nums).append(item)
            if len(set(nums)) != len(nums):
                return False  #数字要不重复
            if len(list(filter(lambda x: len(x) == 0, lists))) != 0:
                return False  #候选列表不能为空集
        return True
    #评分，找到最佳的猜测坐标
    def get_best_point(self):
        best_score = 0
        best_point = (0,0)

        for r, row in enumerate(self.board):
            for c, item in enumerate(row):
                point_score = self.get_point_score((r,c))
                if best_score < point_score:
                    best_score = point_score
                    best_point = (r,c)
        return best_point

    #计算某坐标的评分
    def get_point_score(self, point):
        #评分标准：(10 - 候选个数) + 同行确定数字个数 + 同列确定个数
        r,c = point
        item = self.board[r,c]
        if isinstance(item,list):
            score = 10 - len(item)
            score += sum(map(lambda x: 1 if isinstance(x,int) else 0, self.board[r]))
            score += sum(map(lambda x: 1 if isinstance(x,int) else 0, self.board[:,c]))
            return score
        else:
            return 0
                
    #猜测记录
    def recorder_guess(self, point, index = 0):
        #记录
        recorder = Recorder()
        recorder.point = point
        recorder.point_index = index
        recorder.board = copy.deepcopy(self.board)
        self.recorder.put(recorder)
        self.guess_times += 1 #记录猜测次数

        #新一轮的排除处理
        item = self.board[point]        #获取该点的列表
        self.board[point] = item[index] #填入列表的数字
        self.new_point.put(point)       #将该点加入队列中
        self.solve_sudo()               #继续用普通排除法进行求解
        
    #回溯，需要先进后出
    def reback(self):
        while True:
            #如果这个记录栈为空则报错
            if self.recorder.empty():
                raise Exception('sudo is wrong')
            else:
                recorder = self.recorder.get()
                point = recorder.point
                index = recorder.point_index + 1
                item = recorder.board[point]

                #判断索引是否超出范围。若超出，则再回溯一次
                if index < len(item):
                    break
        self.board = recorder.board
        self.recorder_guess(point, index)
    #解题
    def calc(self):
        #第一次解题
        self.solve_sudo()
        #检查有没有错误的，有错误则回溯；没错误却未解开题目，则再猜测
        while True:
            if self.check_board():
                if self.get_num_count() == 81:
                    break
                else:
                    #获取最佳猜测点
                    point = self.get_best_point()
                    #记录并处理
                    self.recorder_guess(point)
            else:
                #出错，则回溯，尝试下一个猜测
                self.reback()
            

 

###2018－5－12 入门级别
##data = [0,0,2, 8,0,1, 0,7,0,
##        4,0,0, 0,0,0, 0,0,1,
##        5,0,8, 7,0,0, 9,0,4,
##        0,0,0, 6,5,0, 1,4,0,
##        6,2,0, 0,0,0, 3,9,0,
##        1,7,0, 0,3,8, 2,6,0,
##        2,5,3, 4,8,7, 6,1,9,
##        0,0,6, 3,0,9, 7,5,2,
##        0,9,1, 5,0,0, 4,8,3]
###2018－5－12 初级
##data = [0,0,0, 0,0,0, 0,0,0,
##        0,6,0, 3,0,4, 0,2,0,
##        0,0,0, 0,0,0, 0,7,5,
##        0,0,0, 0,0,0, 0,0,0,
##        0,0,0, 6,8,0, 3,0,0,
##        1,0,5, 0,7,0, 0,0,0,
##        0,0,0, 0,5,0, 0,0,0,
##        0,3,0, 0,0,0, 4,0,0,
##        8,0,0, 9,0,0, 0,0,0]
###2018－5－12 中级
##data = [0,0,0, 0,0,0, 0,5,9,
##        0,1,0, 0,0,4, 0,0,0,
##        0,8,0, 1,0,0, 0,0,0,
##        0,0,0, 0,0,0, 4,0,7,
##        5,0,3, 0,6,0, 0,0,0,
##        9,0,0, 0,0,0, 0,0,0,
##        6,0,0, 0,0,0, 0,3,0,
##        0,0,0, 0,0,1, 0,0,0,
##        0,7,0, 8,0,0, 2,0,0]
###2018－5－12 高级
##data = [0,8,0, 0,0,0, 0,0,0,
##        9,0,0, 5,0,0, 7,0,0,
##        0,0,1, 0,0,4, 0,0,2,
##        8,0,0, 0,0,1, 2,0,4,
##        0,0,0, 0,9,0, 0,0,0,
##        0,5,3, 7,0,0, 0,9,0,
##        0,6,0, 0,0,2, 0,8,0,
##        0,0,2, 1,0,0, 0,0,7,
##        0,0,0, 0,0,0, 6,0,0]
#2018－5－12 号称史上最难
data = [8,0,0, 0,0,0, 0,0,0,
        0,0,3, 6,0,0, 0,0,0,
        0,7,0, 0,9,0, 2,0,0,
        0,5,0, 0,0,7, 0,0,0,
        0,0,0, 0,4,5, 7,0,0,
        0,0,0, 1,0,0, 0,3,0,
        0,0,1, 0,0,0, 0,6,8,
        0,0,8, 5,0,0, 0,1,0,
        0,9,0, 0,0,0, 4,0,0]
t1 = time.time()
sudo = Sudo(data)
sudo.calc()
t2 = time.time()
#注：之所以我的猜测次数多，是因为我用的排除法只用了基本排除法
print(u"完成，猜测了%s次" % sudo.guess_times)
print(sudo.board)
print(u"耗时：%.3fs" % (t2-t1))

