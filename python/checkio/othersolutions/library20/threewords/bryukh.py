def checkio(words):
    """
    Split, convert to letters and use a simple search.
    """
    return 'www' in ''.join('d' if w.isdigit() else 'w' for w in words.split())
