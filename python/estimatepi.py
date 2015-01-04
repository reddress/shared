from math import sqrt

def estimate_pi(steps):
    # using only the Pythagorean theorem, estimate pi by repeatedly inscribing
    # regular polygons, starting with a square and doubling the number of
    # sides in each step
    
    # initial values
    side = sqrt(2)  # side of inscribed square on circle of radius 1
    apothem = sqrt(2) / 2  # apothem of this square
    
    for i in range(steps):
        side = sqrt((1-apothem) ** 2 + (side/2) ** 2)
        apothem = sqrt(1 - (side ** 2 / 4))
        
    result = "Estimate for pi in %d steps is %.14f"
    print(result % (steps, pow(2, steps + 1) * side))
    
    return pow(2, steps + 1) * side
