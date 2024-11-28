"""
iterável -> str, range, etc (___iter___)
iterador -> quem sabe entregar um valor por vez
next -> me entrega o proximo valor
iter -> me entrega seu iterador

"""
# for letra in texto
texto = 'Paulo' # interavel
iterador = iter(texto) # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

for letra in texto:
    print(letra)