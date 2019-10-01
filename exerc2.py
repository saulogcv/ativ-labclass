def letras_favoritas(letra, frase):
    tamanho = len(frase)
    quant = 0
    for n in range(0, tamanho):
        if frase[n].lower == letra.lower:
            quant += 1
    print('Sua letra favorita é a letra {} e ela aparece {} vezes na frase "{}"'.format(letra.upper(), quant, frase))

letra = input('Sua letra favorita: ')
frase = input('Uma frase importante: ')

letras_favoritas(letra, frase)
