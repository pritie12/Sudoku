
def init_grid():
    grid= []
    for i in range (9):
        grid.append([])
        for j in range(9):
            grid[i].append(0)
    return grid


def print_grid(g):
     for i in range (9):
        if (i%3==0):
                print("------------" )
        for j in range(9):
            if (j%3==0):
                print("|", end="")
            print(g[i][j], end="")
            
        print("")

def print_arr(arr):
    for i in arr:
        print(i,"|",end="")
    print("")

def check_array(r):
    cheklist=[]
    for i in range(9):
        cheklist.append(False)
    for i in r:
        if cheklist[i-1]:
            return False
        else:
            cheklist[i-1]=True
    return True
def init_array(n,x):
    arr=[]
    for i in range(n):
        arr.append(x)
    return arr

def check_columns(g):
    column_valid=init_array(9,False)
    for i in range(9):
        col = init_array(9,0)
        for j in range(9):
            col[j]=g[j][i]
        column_valid[i]=check_array(col)
    return column_valid

def check_rows(g):
    row_valid=init_array(9,False)
    for i in range(9):
         row_valid[i]=check_array(g[i])
    return row_valid

def check_group(g):
    group_valid=init_array(9,False)
    for i in range(9):
        group=init_array(9,0)
        for j in range(9):
            group[j]=g[3*int(i/3)+int(j/3)][(j%3)+(i%3)*3]
        group_valid[i]=check_array(group)
    return group_valid

    
def test_check_fun():
    g=[ [6,7,2,1,5,3,9,8,4],
        [8,3,1,9,6,4,2,5,7],
        [5,4,9,7,8,2,6,1,3],
        [1,5,7,6,4,9,8,3,2],
        [3,9,6,8,2,1,7,4,5],
        [2,8,4,3,7,5,1,9,6],
        [4,1,5,2,9,6,3,7,8],
        [7,6,3,5,1,8,4,2,9],
        [9,2,8,4,3,7,5,6,1]
    ]
    print("grid")
    print_grid(g)
    print("check row : ", end="")
    print_arr(check_rows(g))
    print("check columns : ", end="")
    print_arr(check_columns(g))
    print("check group : ", end="")
    print_arr(check_group(g))

    
    





def generate_sudoku_grid():
    g=init_grid()
    print_grid(g)
    

print("hello")
generate_sudoku_grid()
test_check_fun()