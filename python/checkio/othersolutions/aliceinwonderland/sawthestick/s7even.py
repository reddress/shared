def checkio(data):
    triangular = []
    n = 0
    i = 1
     
    #make a list of Triangular numbers smaller than data
    while n < data:
        n += i
        i += 1
        if n < data:
            triangular.append(n)
 
    #Test all the numbers start from the longest possibility
    for j in range(len(triangular),0,-1):
        i = 0
        while i+j < len(triangular):
            if sum(triangular[i:i+j+1]) == data:
                return triangular[i:i+j+1]
            i += 1
             
    return []
