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


def strip_and_separate(rhyme):
    """
    Strips the input rhyme of spaces and returns a list of individual lines.
    """
    return "".join([line.replace(" ", "").lower() for line in rhyme]).split("\n")

def pad(grid):
    """
    Fills each line in the list of strings with dots resulting in a rectangle.
    Used to ensure a transposed grid is also a rectangle.
    """
    width = max(map(len, grid))
    return [line.ljust(width, ".") for line in grid]

def transpose(grid):
    # copied from nyncuk's answer to Transposed Matrix in Scientific Expedition
    return list(map(lambda s: "".join(list(s)), zip(*grid)))
    
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
            return (start_row, start_col, start_row, start_col + len(word) - 1)
            
    # if this point is reached, the word was not found.
    return None

def search_vertically(grid, word):
    """
    Search for word in vertical position by transposing the grid and running
    search_horizontally on it. Then, convert coordinates back to original
    arrangement.
    """
    transposed_coords = search_horizontally(transpose(grid), word)
    start_col, start_row, end_col, end_row = transposed_coords

    # rearrange coordinates
    return(start_row, start_col, end_row, end_col)
    
def checkio(rhyme, word):
    grid = pad(strip_and_separate(rhyme))
    return search_horizontally(grid, word) or search_vertically(grid, word)
