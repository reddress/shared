def verif(aposta, sorteados):
    """verif(aposta, sorteados)
    aposta - str "01 02 12 29 30 59"
    sorteados - str as above
    """
    matching = set(map(int, aposta.split())) & set(map(int, sorteados.split()))
    return (len(matching), sorted(matching))

def test():
    testeql(verif("01 02 03 04 05 06", "01 12 13 14 15 16"),
            (1, [1]))
    testeql(verif("01 02 03 04 05 06 07", "01 02 03 04 05 06"),
            (6, [1,2,3,4,5,6]))
    testeql(verif("15 20 03 45 52 60", "03 07 17 33 52 59"),
            (2, [3,52]))
