def checkio(stair_values):
    """Return the best score when traveling up stairs scored by stair_values."""
    # Use dynamic programming to solve this in linear time.
    # Pad initial list to eliminate edge cases.
    values = [0] + stair_values + [0]
    for i in range(1, len(values)):
        values[i] += max(values[i - 1], values[i - 2])
    return values[-1]
