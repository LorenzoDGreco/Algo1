dicc_1 = {'clave1': 1, 'clave3': 3}
dicc_2 = {'clave2': 2, 'clave4': 5}

dicc_1.update(dicc_2)
print(dicc_1)

diccTot = {**dicc_1, **dicc_2}
print(diccTot)