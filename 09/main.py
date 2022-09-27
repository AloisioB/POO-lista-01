class SortMachine:
    def __init__(self):
        self.L = None
        self.R = None

    def RunSortQuick(self, lista):
        if len(lista) > 1:
            mid = len(lista) // 2
            L = lista[:mid]
            R = lista[mid:]
            self.RunSortQuick(L)
            self.RunSortQuick(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    lista[k] = L[i]
                    i += 1
                else:
                    lista[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                lista[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                lista[k] = R[j]
                j += 1
                k += 1
        return lista


    def RunSortSelection(self, lista):
        for i in range(0, len(lista) - 1):
            menor = i
            for j in range(i + 1, len(lista)):
                if lista[j] < lista[menor]:
                    menor = j
            lista[i], lista[menor] = lista[menor], lista[i]
        return lista

S = SortMachine()
print(S.RunSortQuick([1, 2, 4, 5, 0]))
print(S.RunSortSelection([1, 2, 4, 5, 0]))