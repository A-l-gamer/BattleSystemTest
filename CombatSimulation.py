import numpy as np
import time
start_time = time.time()

# Maximum number of forces involved in either side of battle
n = 9
# Quality of the outcome where both players' forces get wiped out
a = 0.25

# Each face is an array [a,b]: a = damage inflicted to defender; b = damage inflicted to attacker.
attackDice = [[0,0], [0,0], [1,0], [1,0], [1,0], [2,1]]
defenceDice = [[0,0], [0,0], [-1,0], [-1,0], [0,1], [-1,1]]

# This iterates produces the probability of reaching each state from the previous one in 1 dice roll
def ChangesMatrix(n,m):
    P = [[0 for j in range(m+1)] for i in range(n+1)]
    P[n][m] = 1
    u = 0
    v = 0
    while(u < n):
        u += 1
        newP = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for d in range(6): # loops over faces of attack dice
            face = attackDice[d]
            for i in range(n+1):
                for j in range(m+1): # loops over all pre-existing options
                    if(P[i][j] != 0): # found a combination that has happened
                        newP[min(max(0,i - face[1]), i)][min(max(0,j - face[0]), j)] +=  P[i][j] / 6           
        P = newP
        
    while(v < m):
        v += 1
        newP = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for d in range(6): # loops over faces of attack dice
            face = defenceDice[d]
            for i in range(n+1):
                for j in range(m+1): # loops over all pre-existing options
                    if(P[i][j] != 0): # found a combination that has happened
                        newP[min(max(0,i - face[1]), i)][min(max(0,j - face[0]), j)] +=  P[i][j] / 6        
        P = newP

    return P          

# This calculates the quality of each outcome by iterating on the quality of each reachable outcome and the probability to reach it                    
def OutcomeMatrix(n,a):
    n += 1
    M = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if(j == 0):
                if(i == 0):
                    M[i][j] = a
                else:
                    M[i][j] = 1
            else:
                if(i == 0):
                    M[i][j] = 0
                else:
                    P = ChangesMatrix(i,j)

                    sumTot = 0
                    for a in range(i):
                        for b in range(j):
                            sumTot += P[a][b]*M[a][b]
                    for a in range(i):
                        sumTot += P[a][j]*M[a][j]
                    for b in range(j):
                        sumTot += P[i][b]*M[i][b]
                    M[i][j] = round(sumTot / (1-P[i][j]),3)
    return M

print(f"The results using \nn = {n} \na = {a}")
print(f"With the dice: \nAttack Dice {attackDice} \nDefence Dice {defenceDice}")
print("")
outcome = np.matrix(OutcomeMatrix(n,a))
print(outcome)
print("--- %s seconds ---" % (time.time() - start_time))
