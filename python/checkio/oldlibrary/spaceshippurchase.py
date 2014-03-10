def checkio(data):
    initial_sofi, raise_sofi, initial_oldman, reduction_oldman = data
    sofia = initial_sofi
    oldman = initial_oldman
    
    while True:
        if sofia >= oldman:
            return sofia
            
        sofia += raise_sofi

        if oldman <= sofia:
            return oldman
        
        oldman -= reduction_oldman 
        print("sofia:", sofia)
        print("oldman:", oldman)

checkio([150, 50, 1000, 100])
checkio([500, 300, 700, 100])
