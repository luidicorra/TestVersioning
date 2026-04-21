# script_conta_parole.py

def conta_parole(testo):
    parole = testo.split()
    return len(parole)

# Esempio di utilizzo
frase = "Python è semplice e potente"
numero_parole = conta_parole(frase)
print(f"Numero di parole: {numero_parole}")