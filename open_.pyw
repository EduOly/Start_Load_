import shelve
import os

arq_start = shelve.open('path_')

lista_arq = list(arq_start.keys())

for c in range(len(lista_arq)):

    os.system(arq_start[lista_arq[c]])

arq_start.close()
