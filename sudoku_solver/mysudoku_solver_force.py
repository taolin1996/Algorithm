##myinput = [[0, 9, 5, 0, 2, 0, 0, 6, 0],
##           [0, 0, 7, 1, 0, 3, 9, 0, 2],
##           [6, 0, 0, 0, 0, 5, 3, 0, 4],
##           [0, 4, 0, 0, 1, 0, 6, 0, 7],
##           [5, 0, 0, 2, 0, 7, 0, 0, 9],
##           [7, 0, 3, 0, 9, 0, 0, 2, 0],
##           [0, 0, 9, 8, 0, 0, 0, 0, 6],
##           [8, 0, 6, 3, 0, 2, 1, 0, 5],
##           [0, 5, 0, 0, 7, 0, 2, 8, 3]]
myinput = [[0,0,5,3,0,0,0,0,0],
           [8,0,0,0,0,0,0,2,0],
           [0,7,0,0,1,0,5,0,0],
           [4,0,0,0,0,5,3,0,0],
           [0,1,0,0,7,0,0,0,6],
           [0,0,3,2,0,0,0,8,0],
           [0,6,0,5,0,0,0,0,9],
           [0,0,4,0,0,0,0,3,0],
           [0,0,0,0,0,9,7,0,0]]

sudokubackup = [[set(),set(),set(),set(),set(),set(),set(),set(),set()],
                [set(),set(),set(),set(),set(),set(),set(),set(),set()],
                [set(),set(),set(),set(),set(),set(),set(),set(),set()],
                [set(),set(),set(),set(),set(),set(),set(),set(),set()],
                [set(),set(),set(),set(),set(),set(),set(),set(),set()],
                [set(),set(),set(),set(),set(),set(),set(),set(),set()],
                [set(),set(),set(),set(),set(),set(),set(),set(),set()],
                [set(),set(),set(),set(),set(),set(),set(),set(),set()],
                [set(),set(),set(),set(),set(),set(),set(),set(),set()]]
class point:  
    def __init__(self,x,y):  
        self.row=x  
        self.column=y  
        self.available=[]  
        self.value=0

def updateset(board,Set,p_row,p_column):
    setall = set({0,1,2,3,4,5,6,7,8,9})
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 0):
                Set[i][j] = set()
                Set[i][j].update(set(row(i)))
                Set[i][j].update(set(column(j)))
                Set[i][j].update(set(gong(i,j)))
                Set[i][j] = setall.difference(Set[i][j])
            else:
                Set[i][j] = set()
    return list(Set[p_row][p_column])
                
def initpoint(board):
    pointlist = []
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 0):
                p = point(i,j)
                for k in range(1,10):
                    if (k not in row(i)) and (k not in column(j)) and (k not in gong(i,j)):
                        p.available.append(k)
                pointlist.append(p)
    return pointlist
def row(j):
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
def check(p, board):
    if(p.value == 0):
        return False
    if(p.value not in row(p.row)) and (p.value not in column(p.column)) and (p.value not in gong(p.row,p.column)):
        return True
    else:
        return False
def InputMysudoku(board):
    for i in range(9):
        temp = input().split(" ")
        temp = [int(j) for j in temp]
        board.append(temp)
def Calculatemysudoku(p, board):
    global pointList
    #print("Enter Calculatemysudoku")
    availist = p.available
    #print("p.row =",p.row,"p.column =",p.column," ",availist)
    for i in availist:
        p.value = i
        if(check(p, board)):
            #print("check(",p.row,p.column,p.value,")")
            board[p.row][p.column] = p.value
            #填上数后如何剔除掉候选区的矛盾元素？
            #outputmysudoku(board)
            if(len(pointList) == 0):
                print()
                outputmysudoku(board)
                return 
                
            ptemp = pointList.pop()
            #ptemp.available = list(updateset(board, sudokubackup, ptemp.row, ptemp.column))
            
            #print("ptemp =(",ptemp.row, ptemp.column, ptemp.value,")","len(pointList) =",len(pointList))
            Calculatemysudoku(ptemp, board)
            board[p.row][p.column] = 0
            board[ptemp.row][ptemp.column] = 0
            ptemp.value = 0
            pointList.append(ptemp)
        else:
            pass
    #print("Exit Calculatemysudoku")
    
def outputmysudoku(board):
    for i in range(9):
        for j in range(9):
            if(j == 8):
                print(board[i][j])
            else:
                print(board[i][j], end=" ")

pointList = initpoint(myinput)
p = pointList.pop()
Calculatemysudoku(p,myinput)

