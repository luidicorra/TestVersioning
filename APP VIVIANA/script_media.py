# script_media.py

def calcola_media(numeri):
    if not numeri:
        return 0
    return sum(numeri) / len(numeri)

# Esempio di utilizzo
lista_numeri = [10, 20, 30, 40]
media = calcola_media(lista_numeri)
print(f"La media è: {media}")