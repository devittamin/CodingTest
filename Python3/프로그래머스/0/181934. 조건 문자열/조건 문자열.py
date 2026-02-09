
   
def solution(ineq, eq, n, m):
    if ineq == ">" and eq == "=":
        return 1 if n >= m else 0
    elif ineq == "<" and eq == "=":
        return 1 if n <= m else 0
    elif ineq == ">" and eq == "!":
        return 1 if n > m else 0
    elif ineq == "<" and eq == "!":
        return 1 if n < m else 0

    
    '''
같코
    def solution(ineq, eq, n, m):
    if eq == "=":
        return 1 if (n >= m if ineq == ">" else n <= m) else 0
    else:
        return 1 if (n > m if ineq == ">" else n < m) else 0

    '''