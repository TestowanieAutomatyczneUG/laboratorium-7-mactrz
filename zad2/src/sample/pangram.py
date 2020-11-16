class Pangram:

    def check(self, napis):
        wynik = True
        lista = []
        alfa = 'abcdefghijklmnopqrstuvwxyz'
        if type(napis) != str:
            raise Exception("Error in Pangram")
        for x in napis:
            if lista.count(x.lower()) == 0:
                lista.append(x.lower())
        for i in alfa:
            if lista.count(i) == 0:
                wynik = False
        return wynik