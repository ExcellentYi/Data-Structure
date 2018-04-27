maxsize = 0
size = 0
cntarr = []

def get_value(A,i,j,L,H):
    if (i<0 or i>=L or j<0 or j>=H):
        return 0
    else:
        return A[i][j]

def find_max_block(A,r,c,L,H,size):
    global maxsize
    global cntarr
    if(r>=L or c>=H):
        return
    cntarr[r][c] = 1
    size += 1
    if(size > maxsize):
        maxsize = size
    
    direction = [[-1,0],[-1,-1],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for i in range(0,8):
        newi = r+direction[i][0]
        newj = c+direction[i][1]
        val = get_value(A,newi,newj,L,H)

        if(val>0 and (cntarr[newi][newj] == 0)):
            find_max_block(A,newi,newj,L,H,size)
    cntarr[r][c] = 0

def get_max_ones(A,rmax,colmax):
    global maxsize
    global size
    global cntarr
    for i in range(0,rmax):
        for j in range(0,colmax):
            if(A[i][j] == 1):
                find_max_block(A,i,j,rmax,colmax,0)
    return maxsize


zarr = [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]
rmax = 5
colmax = 5
cntarr = [[0 for i in range(5) ] for j in range(5)]
print('Number of maximum 1s are ')
print(get_max_ones(zarr,rmax,colmax))



