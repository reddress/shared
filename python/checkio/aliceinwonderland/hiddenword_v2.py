rhyme1 = """DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?"""

rhyme2 = """He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!"""


# Corrected several points noted by Cjkjvfnby
def make_line_grid(rhyme):
    """
    Strip the input rhyme of spaces, and create a list of padded lines.
    The padding ensures that transposing the grid results in a rectangle.
    """
    lines = "".join([char.replace(" ", "").lower() for char in rhyme]).split("\n")
    width = max(map(len, lines))
    return [line.ljust(width, ".") for line in lines]

def transpose(grid):
    # copied from nyncuk's answer to Transposed Matrix in Scientific Expedition
    return list(map(lambda s: "".join(s), zip(*grid)))
    
def search_horizontally(grid, word):
    """
    Return the row and column of the location of word, if found
    """
    for row, line in enumerate(grid):
        find_col = line.find(word)
        # since find returns -1 if word is not found, add 1 to artificially
        # create a False value if the word is not found.
        if find_col + 1:
            start_row = row + 1
            start_col = find_col + 1
            return start_row, start_col, start_row, start_col + len(word) - 1
            
    # if this point is reached, the word was not found.
    return None

def search_vertically(grid, word):
    """
    Search for word in vertical position by transposing the grid and running
    search_horizontally on it. Then, convert coordinates back to original
    arrangement.
    """
    # rearrange result's coordinates
    def transpose_coords(x1, x2, y1, y2):
        return x2, x1, y2, y1

    try:
        return transpose_coords(*search_horizontally(transpose(grid), word))
    except TypeError:
        return None
    
def checkio(rhyme, word):
    grid = make_line_grid(rhyme)
    return search_horizontally(grid, word) or search_vertically(grid, word)

checkio(rhyme1, "ten")
checkio(rhyme2, "noir")
