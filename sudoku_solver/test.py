##myinput = [[0, 9, 2, 4, 8, 1, 7, 6, 3],
##           [4, 1, 3, 7, 6, 2, 9, 8, 5],
##           [8, 6, 7, 3, 5, 9, 4, 1, 2],
##           [6, 2, 4, 1, 9, 5, 3, 7, 8],
##           [7, 5, 9, 8, 4, 3, 1, 2, 6],
##           [1, 3, 8, 6, 2, 7, 5, 9, 4],
##           [2, 7, 1, 5, 3, 8, 6, 4, 9],
##           [3, 8, 6, 9, 1, 4, 2, 5, 7],
##           [0, 4, 5, 2, 7, 6, 8, 3, 1]]
myinput = [[0, 9, 5, 0, 2, 0, 0, 6, 0],
           [0, 0, 7, 1, 0, 3, 9, 0, 2],
           [6, 0, 0, 0, 0, 5, 3, 0, 4],
           [0, 4, 0, 0, 1, 0, 6, 0, 7],
           [5, 0, 0, 2, 0, 7, 0, 0, 9],
           [7, 0, 3, 0, 9, 0, 0, 2, 0],
           [0, 0, 9, 8, 0, 0, 0, 0, 6],
           [8, 0, 6, 3, 0, 2, 1, 0, 5],
           [0, 5, 0, 0, 7, 0, 2, 8, 3]]
##myinput = [[0,0,5,3,0,0,0,0,0],
##           [8,0,0,0,0,0,0,2,0],
##           [0,7,0,0,1,0,5,0,0],
##           [4,0,0,0,0,5,3,0,0],
##           [0,1,0,0,7,0,0,0,6],
##           [0,0,3,2,0,0,0,8,0],
##           [0,6,0,5,0,0,0,0,9],
##           [0,0,4,0,0,0,0,3,0],
##           [0,0,0,0,0,9,7,0,0]]
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

def forcesolve(board,Set):
    if(issolved(board) == True):
        OutputMysudoku(board)
        return
    else:
        for i in range(9):
            for j in range(9):
                if(board[i][j] == 0):
                    updateset(board, Set)
                    for k in range(len(Set[i][j])):
                        #判断数独是否无解，若无解，直接返回
                        print("Set[",i,"][",j,"] =",Set[i][j])
                        board[i][j] = Set[i][j].pop()
                        print("board[i][j] =",board[i][j])
                        OutputMysudoku(board)
                        updateset(board, Set)
                        forcesolve(board,Set)

                    
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
        
def CalculateSudoku(board):
    print("Enter CalculateSudoku")
    global sudokubackup
    global Flag_IsFillElem
    #判断上次递归的数独是否填入数字
    #没填入就暴力求解
    Flag_IsFillElem = 0
    #如果不相同就继续用常规套路求解
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 0):
                solvespecielem(board,i,j)
    if(Flag_IsFillElem == 0): #没填入数，开始暴力求解
        #forcesolve()
        print(sudokubackup)
    #OutputMysudoku()
    #print(sudokubackup)
    #print("IsFillElem =", Flag_IsFillElem)
    if(issolved(board) == False):
        CalculateSudoku(board)
    print("Exit CalculateSudoku")

def issolved(board):
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 0):
                return False
    return True

def doeshassolution(board):
    for i in range(9):
        for j in range(9):
            x = set(raw(i))
            y = set(column(j))
            if((x&y!={0})or(x&y != {})):
                return False  #无解
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

#InputMysudoku()
#OutputMysudoku(myinput)
#print()
##CalculateSudoku(myinput)
#forcesolve(myinput, sudokubackup)
#OutputMysudoku(myinput)
print(doeshassolution(myinput))

##for i in range(9):
##    for j in range(9):
##        if(myinput[i][j] == 0):
##            solvespecielem(i,j)

