def checkio(steps):
    def move(sum, steps):
        try:
            return max(move(sum + steps[1], steps[1:]),  # move one step only
                       move(sum + steps[2], steps[2:]))  # jump over a step
        except IndexError:
            return sum
    return move(0, [0] + steps + [0])  # add start and end platforms

checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27])
checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95])
