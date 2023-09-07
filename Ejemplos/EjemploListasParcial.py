def aprobo_cursada1(lista_total, lista_puntajes):
    aprobo = False
    
    nota_tot = sum(lista_total)
    nota_puntajes = sum(lista_puntajes)
    resultado = (nota_puntajes * 100) / nota_tot
    
    if(resultado >= 60):
        aprobo = True
    return aprobo

def aprobo_cursada(lista_total, lista_puntajes):
    return (sum(lista_puntajes) * 100) / sum(lista_total) >= 60
    
print(aprobo_cursada([10,20,15],[6,15,12]))
print(aprobo_cursada([10,20,15],[6,8,12]))
print(aprobo_cursada([10,20,15,30],[6,13,9,12]))