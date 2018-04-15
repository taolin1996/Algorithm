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
myinput = [[0,0,5,3,0,0,0,0,0],
           [8,0,0,0,0,0,0,2,0],
           [0,7,0,0,1,0,5,0,0],
           [4,0,0,0,0,5,3,0,0],
           [0,1,0,0,7,0,0,0,6],
           [0,0,3,2,0,0,0,8,0],
           [0,6,0,5,0,0,0,0,9],
           [0,0,4,0,0,0,0,3,0],
           [0,0,0,0,0,9,7,0,0]]
        
def solvespecielem(i,j):
    setall = set({0,1,2,3,4,5,6,7,8,9})
    settemp = set()
    settemp.update(set(raw(i)))
    settemp.update(set(column(j)))
    settemp.update(set(gong(i,j)))
    if(len(setall.difference(settemp)) == 1):
        myinput[i][j] = int(list(setall.difference(settemp))[0])
def CalculateSudoku():
    for i in range(9):
        for j in range(9):
            if(myinput[i][j] == 0):
                solvespecielem(i,j)
    if(issolved() == False):
        print("Not Solved!")
        CalculateSudoku()

def issolved():
    for i in range(9):
        for j in range(9):
            if(myinput[i][j] == 0):
                return False
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
            #print(myinput[x][y], end = " ")
            ok.append(myinput[x][y])
    return ok
def OutputMysudoku():
    for i in range(9):
        for j in range(9):
            print(myinput[i][j], end = ' ')
        print()

#InputMysudoku()
OutputMysudoku()
print()
CalculateSudoku()
OutputMysudoku()
