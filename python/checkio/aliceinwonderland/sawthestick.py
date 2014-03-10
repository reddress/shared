from math import ceil, sqrt

def tri_num_sequence(limit):
    """
    Return a list of all triangular numbers smaller than or equal to limit.
    """
    
    # From Wikipedia: nth triangular number is n(n + 1) / 2.
    # First rearranging "limit = n(n + 1) / 2" to a quadratic equation,
    # the positive solution, using the quadratic formula, gives
    # the index of the last desired triangular number.
    n = ceil((sqrt(1 + 8 * limit) - 1) / 2)

    sequence = []
    for i in range(n):
        sequence.append(int((i * (i + 1)) / 2))
    return sequence[1:]  # omit the initial 0 value

def checkio(number):
    """
    Find the consecutive fragment of triangular numbers with maximum quantity
    """
    tri_nums = tri_num_sequence(number)

    # Define starting point for fragment search, exhaustively
    # search all combinations. Begin searching from low values to find the
    # combination yielding the greatest quantity of segments.
    for start_point in range(len(tri_nums)):
        end_point = start_point + 1
        fragment_sum = 0
        
        while end_point <= len(tri_nums) and fragment_sum < number:
            fragment_sum = sum(tri_nums[start_point:end_point])
            if fragment_sum == number:
                print("found: ", number, tri_nums)
                return tri_nums[start_point:end_point]
            end_point += 1
            
    # else nothing was found
    return []

checkio(64)
checkio(10)
tri_num_sequence(11)
checkio(10)
