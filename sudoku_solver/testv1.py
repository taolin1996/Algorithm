import time
##myinput = [[0, 9, 2, 4, 8, 1, 7, 6, 3],
##           [4, 1, 3, 7, 6, 2, 9, 8, 5],
##           [8, 6, 7, 3, 5, 9, 4, 1, 2],
##           [6, 2, 4, 1, 9, 5, 3, 7, 8],
##           [7, 5, 9, 8, 4, 3, 1, 2, 6],
##           [1, 3, 8, 6, 2, 7, 5, 9, 4],
##           [2, 7, 1, 5, 3, 8, 6, 4, 9],
##           [3, 8, 6, 9, 1, 4, 2, 5, 7],
##           [0, 4, 5, 2, 7, 6, 8, 3, 1]]
##myinput = [[0, 9, 5, 0, 2, 0, 0, 6, 0],
##           [0, 0, 7, 1, 0, 3, 9, 0, 2],
##           [6, 0, 0, 0, 0, 5, 3, 0, 4],
##           [0, 4, 0, 0, 1, 0, 6, 0, 7],
##           [5, 0, 0, 2, 0, 7, 0, 0, 9],
##           [7, 0, 3, 0, 9, 0, 0, 2, 0],
##           [0, 0, 9, 8, 0, 0, 0, 0, 6],
##           [8, 0, 6, 3, 0, 2, 1, 0, 5],
##           [0, 5, 0, 0, 7, 0, 2, 8, 3]]
##myinput = [[0,0,5,3,0,0,0,0,0],
##           [8,0,0,0,0,0,0,2,0],
##           [0,7,0,0,1,0,5,0,0],
##           [4,0,0,0,0,5,3,0,0],
##           [0,1,0,0,7,0,0,0,6],
##           [0,0,3,2,0,0,0,8,0],
##           [0,6,0,5,0,0,0,0,9],
##           [0,0,4,0,0,0,0,3,0],
##           [0,0,0,0,0,9,7,0,0]]
myinput = [[3,9,5,7,2,4,8,6,1],
           [4,8,7,1,6,3,9,5,2],
           [6,2,1,9,8,5,3,7,4],
           [0,4,0,5,1,8,6,3,7],
           [5,6,8,2,3,7,4,1,9],
           [7,1,3,4,9,6,5,2,8],
           [0,3,0,8,5,1,7,4,6],
           [8,7,6,3,4,2,1,9,5],
           [1,5,4,6,7,9,2,8,3]]
sudokubackup = [[set(),set(),set(),set(),set(),set(),set(),set(),set()],
                [set(),set(),set(),set(),set(),set(),set(),set(),set()],
                [set(),set(),set(),set(),set(),set(),set(),set(),set()],
                [set(),set(),set(),set(),set(),set(),set(),set(),set()],
                [set(),set(),set(),set(),set(),set(),set(),set(),set()],
                [set(),set(),set(),set(),set(),set(),set(),set(),set()],
                [set(),set(),set(),set(),set(),set(),set(),set(),set()],
                [set(),set(),set(),set(),set(),set(),set(),set(),set()],
                [set(),set(),set(),set(),set(),set(),set(),set(),set()]]
Flag_IsFillElem = 0
#常规套路，将当前行列中符合要求的元素添加到其对应的集合中
def updateset(board,Set):
    setall = set({0,1,2,3,4,5,6,7,8,9})
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 0):
                Set[i][j] = set()
                Set[i][j].update(set(raw(i)))
                Set[i][j].update(set(column(j)))
                Set[i][j].update(set(gong(i,j)))
                Set[i][j] = setall.difference(Set[i][j])
            else:
                Set[i][j] = set()

def forcesolve(board,Set,p,q):
    print("Enter forcesolve(board,Set,",p,q,")")
    if(issolved(board) == True):
        print("Is Solved!")
        OutputMysudoku(board)
        print()
        return
    elif(hassolution(board) == False):
        print("Has No solution!")
        print("Exit forcesolve(board,Set,",p,q,")")
        return
    else:
        updateset(board,Set)
        for i in range(9):
            for j in range(9):
                if(board[i][j] == 0):
                    templist = list(Set[i][j])
                    for k in templist:
                        board[i][j] = k
                        forcesolve(board, Set, i, j)
                        board[i][j] = 0
                        board[p][q] = 0
                    #OutputMysudoku(board)
                    print("Exit forcesolve(board,Set,",p,q,")")
                    return
                             
def solvespecielem(board,i,j):
    global sudokubackup
    global Flag_IsFillElem
    setall = set({0,1,2,3,4,5,6,7,8,9})
    sudokubackup[i][j] = set()
    sudokubackup[i][j].update(set(raw(i)))
    sudokubackup[i][j].update(set(column(j)))
    sudokubackup[i][j].update(set(gong(i,j)))
    sudokubackup[i][j] = setall.difference(sudokubackup[i][j])
    if(len(sudokubackup[i][j]) == 1):#每填一个数都要更新一下备用集合
        board[i][j] = list(sudokubackup[i][j])[0]
        #print("position is",i,j,"Enter num is",list(sudokubackup[i][j])[0])
        updateset(board,sudokubackup)
        Flag_IsFillElem = 1
        
def CalculateSudoku(board,Set):
    print("Enter CalculateSudoku")
    global Flag_IsFillElem
    #判断上次递归的数独是否填入数字
    #没填入就暴力求解
    Flag_IsFillElem = 0
    #如果不相同就继续用常规套路求解
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 0):
                solvespecielem(board,i,j)
                tempi, tempj = i , j
    if(Flag_IsFillElem == 0): #没填入数，开始暴力求解
        #forcesolve(board,Set, tempi, tempj)
        print(sudokubackup)
    #OutputMysudoku()
    #print(sudokubackup)
    #print("IsFillElem =", Flag_IsFillElem)
    if(issolved(board) == False):
        CalculateSudoku(board,Set)
    print("Exit CalculateSudoku")

def issolved(board):
    for i in range(1,10):
        for j in range(9):
            tempraw = raw(j)
            if(i not in tempraw):
                return False
        for j in range(9):
            tempcolumn = column(j)
            if(i not in tempcolumn):
                return False
        for j in range(3):
            for k in range(3):
                tempgong = gong(j,k)
                if(i not in tempgong):
                    return False #未被解决       
    return True 

def InputMysudoku():
    for i in range(9):
        temp = input().split(" ")
        temp = [int(j) for j in temp]
        myinput.append(temp)
        
def raw(j):
    ok = []
    for i in range(9):
        ok.append(myinput[j][i])
    return ok

def column(j):
    ok = []
    for i in range(9):
        ok.append(myinput[i][j])
    return ok

def gong(i,j):
    ok = []
    p = int(i/3)
    q = int(j/3)
    g = q*3+p  #计算出第几宫 
    for x in range(int(g%3)*3,int(g%3)*3+3):
        for y in range(int(g/3)*3,int(g/3)*3+3):
            ok.append(myinput[x][y])
    return ok

def OutputMysudoku(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end = ' ')
        print()

def hassolution(board):
    for i in range(1,10):
        for j in range(9):
            tempraw = raw(j)
            if(tempraw.count(i) > 1):
                return False
        for j in range(9):
            tempcolumn = column(j)
            if(tempcolumn.count(i) > 1):
                return False
        for j in range(3):
            for k in range(3):
                tempgong = gong(j,k)
                if(tempgong.count(i) > 1):
                    return False #肯定无解          
    return True 
#InputMysudoku()
OutputMysudoku(myinput)
print()
start = time.time()
#CalculateSudoku(myinput,sudokubackup)
forcesolve(myinput, sudokubackup, 3, 0)
#OutputMysudoku(myinput)
#print(issolved(myinput))
print("Time Used:", time.time()-start)


##for i in range(9):
##    for j in range(9):
##        if(myinput[i][j] == 0):
##            solvespecielem(i,j)

