n = 5;
f = [ [0]*n, [0]*n ];
#e = ( (1), (1) );
#x = ( (1), (1) );

##a = ( (1,4,5,8,9), (2,3,6,7,10) );
#a = ( (1,3,1,1,1), (1,1,4,1,1) );
#t = ( (1,1,1,1), (1,1,1,1) );

e = ( (1), (1), (1) );
x = ( (1), (1), (1) );

#a = ( (1,4,5,8,9), (2,3,6,7,10) );
a = ( (1,3,1,3,1), (1, 1,4, 2,1), (1, 1,1, 1,1) );
t = ( (1,1,1,1), (1,1,1,1), (1,1, 1,1) );

def Fastest_Way(f,a,t,e,x,n):
    f[0][0] = e[0] + a[0][0]
    f[1][0] = e[1] + a[1][0]
    path = [ [3]* n, [3]*n ]
    print path
    for j in range(1,n):
        # checking, line 0 station 1 
        if (f[0][j-1] + a[0][j]) <= (f[1][j-1] + t[1][j-1] + a[0][j]):
            # Adding line 0 station 1 to f
            f[0][j] = f[0][j-1] + a[0][j]
            # remembering path we followed
            path[0][j-1] = 0
        else:
            f[0][j] = f[1][j-1] + t[1][j-1] + a[0][j]
            path[0][j-1] = 1

        # Checking, line 1 station 1
        if (f[1][j-1] + a[1][j]) <= (f[0][j-1] + t[0][j-1] + a[1][j]):
            # Adding line 1 station 1 to f
            f[1][j] = f[1][j-1] + a[1][j]
            # Remembering path we followed
            path[1][j-1] = 1
        else:
            f[1][j] = f[0][j-1] + t[0][j-1] + a[1][j]
            path[1][j-1] = 0

    # Differentiating which starting node was best
    # Cuz we start froms diff node, then take best path for that start
    if f[0][n-1] + x[0] <= f[1][n-1] + x[1]:
        print "optimal time in f[0] " + str(f[0][n-1] + x[0])
        print "path before "  
        print path
        path[0][n-1] = 0
        print path
        print f
    else:
        print "optimal time in f[1] " + str(f[1][n-1] + x[1])
        print "path before "  
        print path
        path[1][n-1] = 1
        print path
        print f

def linePath(a,t,x,e,n):
    
    #fastestTime = min(calcPath(a,t,x,e,n, 0, n-1) + x[0], calcPath(a,t,x,e,n, 1, n-1) + x[1])
    return min(calcPath(a,t,x,e, 0, n-1) + x[0], calcPath(a,t,x,e, 1, n-1) + x[1])

def calcPath(a,t,x,e, f, j):
    if f == 0:
        if j == 0:
            return a[0][0] + e[0]
        return min (calcPath(a,t,x,e, 0, j-1) + a[0][j], calcPath(a,t,x,e, 1, j-1) + t[1][j-1] + a[0][j])

    elif f == 1:
        if j == 0:
            return a[1][0] + e[1]
        return min (calcPath(a,t,x,e, 1, j-1) + a[1][j], calcPath(a,t,x,e, 0, j-1) + t[0][j-1] + a[1][j])
    
# AP Lab Task 1 (Recursion)
def three_lane(a,t,x,e,n):
    
    #fastestTime = min(calcPath(a,t,x,e,n, 0, n-1) + x[0], calcPath(a,t,x,e,n, 1, n-1) + x[1])
    return min(node(a,t,x,e, 0, n-1) + x[0],
               node(a,t,x,e, 1, n-1) + x[1],
               node(a,t,x,e, 2, n-1) + x[2])

def node(a,t,x,e, f, j):
    if f == 0:
        if j == 0:
            return a[0][0] + e[0]
        return min (node(a,t,x,e, 0, j-1) + a[0][j], node(a,t,x,e, 1, j-1) + t[1][j-1] + a[0][j],
                    node(a,t,x,e, 2, j-1) + t[2][j-1] + a[0][j])

    elif f == 1:
        if j == 0:
            return a[1][0] + e[1]
        return min (node(a,t,x,e, 1, j-1) + a[1][j], node(a,t,x,e, 0, j-1) + t[0][j-1] + a[1][j],
                    node(a,t,x,e, 2, j-1) + t[2][j-1] + a[1][j])

    elif f == 2:
        if j == 0:
            return a[2][0] + e[2]
        return min (node(a,t,x,e, 2, j-1) + a[2][j], node(a,t,x,e, 0, j-1) + t[0][j-1] + a[2][j],
                    node(a,t,x,e, 1, j-1) + t[1][j-1] + a[1][j])


# AP Lab Task 2 (Recursion + memoization)
def three_lane_mem(f,a,t,x,e,n):
    
    #fastestTime = min(calcPath(a,t,x,e,n, 0, n-1) + x[0], calcPath(a,t,x,e,n, 1, n-1) + x[1])
    return min(nodeMem(f,a,t,x,e, 0, n-1) + x[0],
               nodeMem(f,a,t,x,e, 1, n-1) + x[1],
               nodeMem(f,a,t,x,e, 2, n-1) + x[2])

def nodeMem(f,a,t,x,e, lane, j):
    if f[lane][j] is not None:
        return f[lane][j]
    if lane == 0:
        #if f[lane][j] is not None:
            #return f[lane][j]
        if j == 0:
            return a[0][0] + e[0]
        f[lane][j-1] = nodeMem(f,a,t,x,e, 0, j-1)
        f[1][j-1] = nodeMem(f,a,t,x,e, 1, j-1)
        f[2][j-1] = nodeMem(f,a,t,x,e, 2, j-1)
        return min (f[lane][j-1] + a[0][j], f[1][j-1] + t[1][j-1] + a[0][j],
                    f[2][j-1] + t[2][j-1] + a[0][j])

    elif lane == 1:
        if j == 0:
            return a[1][0] + e[1]
        f[0][j-1] = nodeMem(f,a,t,x,e, 0, j-1)
        f[lane][j-1] = nodeMem(f,a,t,x,e, 1, j-1)
        f[2][j-1] = nodeMem(f,a,t,x,e, 2, j-1)
        return min (f[lane][j-1] + a[1][j], f[0][j-1] + t[0][j-1] + a[1][j],
                    f[2][j-1] + t[2][j-1] + a[1][j])

    elif lane == 2:
        if j == 0:
            return a[2][0] + e[2]
        f[0][j-1] = nodeMem(f,a,t,x,e, 0, j-1)
        f[1][j-1] = nodeMem(f,a,t,x,e, 1, j-1)
        f[lane][j-1] = nodeMem(f,a,t,x,e, 2, j-1)
        return min (f[lane][j-1] + a[2][j], f[0][j-1] + t[0][j-1] + a[2][j],
                    f[1][j-1] + t[1][j-1] + a[1][j])

# AP Lab Task 3 (dynamic programming) iterative
def three_lane_itr(f,a,t,e,x,n):
    f[0][0] = e[0] + a[0][0]
    f[1][0] = e[1] + a[1][0]
    f[2][0] = e[2] + a[2][0]
    path = [ [7]* n, [7]*n, [7]*n ]
    for j in range(1,n):
        # Lane 1
        v1 = f[0][j-1] + a[0][j]
        v2 = f[1][j-1] + t[1][j-1] + a[0][j]
        v3 = f[2][j-1] + t[2][j-1] + a[0][j]
        if v1 == min (v1, v2, v3):
            f[0][j] = v1
            path[0][j-1] = 0
        elif v2 == min(v1, v2, v3):
            f[0][j] = v2
            path[0][j-1] = 1
        elif v3 == min(v1, v2, v3):
            f[0][j] = v3
            path[0][j-1] = 2

        # Lnae 2
        v1 = f[0][j-1] + t[0][j-1] + a[1][j]
        v2 = f[1][j-1] + a[1][j]
        v3 = f[2][j-1] + t[2][j-1] + a[1][j]
        if v1 == min (v1, v2, v3):
            f[1][j] = v1
            path[1][j-1] = 0
        elif v2 == min(v1, v2, v3):
            f[1][j] = v2
            path[1][j-1] = 1
        elif v3 == min(v1, v2, v3):
            f[1][j] = v3
            path[1][j-1] = 2

        # Lane 3
        v1 = f[0][j-1] + t[0][j-1] + a[2][j]
        v2 = f[1][j-1] + t[1][j-1] + a[2][j]
        v3 = f[2][j-1] + a[2][j]
        if v1 == min (v1, v2, v3):
            f[2][j] = v1
            path[2][j-1] = 0
        elif v2 == min(v1, v2, v3):
            f[2][j] = v2
            path[2][j-1] = 1
        elif v3 == min(v1, v2, v3):
            f[2][j] = v3
            path[2][j-1] = 2

    v1 = f[0][n-1] + x[0]
    v2 = f[1][n-1] + x[1]
    v3 = f[2][n-1] + x[2]
    if v1 == min (v1, v2, v3):
        print "optimal path: " + str(v1)
    elif v2 == min (v1, v2, v3):
        print "optimal path: " + str(v2)
    elif v3 == min (v1, v2, v3):
        print "optimal path: " + str(v3)


if __name__ == '__main__':

    print "!!! Welcome to AP Lab 6 !!!"
    print "Task 1"
    print "This is the simulation of 3-lane assembly line via recursive solution"
    print three_lane(a,t,x,e,n)
    print "Task 2"
    f = [ [None]*n, [None]*n, [None]*n ]
    print "This is the simulation of 3-lane assembly line via recursive solution plus memoization"
    print three_lane_mem(f,a,t,x,e,n)
    print "Task 3"
    f2 = [ [0]*n, [0]*n, [0]*n ]
    print "This is the simulation of 3-lane assembly line via dynamic programming (iterative)"
    print three_lane_itr(f2,a,t,x,e,n)

    #Fastest_Way(f,a,t,x,e,n)