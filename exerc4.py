media_bbt_i = 0
media_bbt_n = 0
media_bb_i = 0
media_bb_n = 0
media_fr_i = 0
media_fr_n = 0
media_bm_i = 0
media_bm_n = 0
quant_bbt = 0
quant_bb = 0
quant_fr = 0
quant_bm = 0
ep_09 = 0
ep_19 = 0
def verificar_ano(data):
    lista = data.split(' ')
    return(lista[2])

with open('series.csv', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        
        separado = line.split(',')
        if int(separado[5]) == 10 and int(separado[6])==10:
            print('Série: ', separado[0])
            print('Episódio: Temporada {}, Ep {}'.format(separado[1], separado[2]))
            print('Nota IMDB: ', separado[5])
            print('Nota Netflix: ', separado[6])
       
        ano = verificar_ano(separado[3])
        
        if int(ano)>=10 and int(ano)<=19:
            ep_19 = ep_19 + 1
        else:
            ep_09 = ep_09 + 1

         
     
        if separado[0] == 'The Big Bang Theroy':
            media_bbt_i += int(separado[5])
            media_bbt_n += int(separado[6])
            quant_bbt += 1
        elif separado[0] == 'Friends':
            media_fr_i += int(separado[5])
            media_fr_n += int(separado[6])
            quant_fr += 1
        elif separado[0] == 'Breaking Bad':
            media_bb_i += int(separado[5])
            media_bb_n += int(separado[6])
            quant_bb += 1
        elif separado[0] == 'Black Mirror':
            media_bm_i += int(separado[5])
            media_bm_n += int(separado[6])
            quant_bm += 1


    print('Número de episódios até 2009: ', ep_09)
    print('Número de episódios entre 2010 e 2019: ', ep_19)
    print()
    print('Black Mirror:         {}(IMDB)  {}(Netflix)'.format(round(media_bm_i/quant_bm, 2), round(media_bm_i/quant_bm, 2)))
    print('Breaking Bad:         {}(IMDB)  {}(Netflix)'.format(round(media_bb_i/quant_bb, 2), round(media_bb_n/quant_bb, 2)))
    print('The Big Bang Theory:  {}(IMDB)  {}(Netflix)'.format(round(media_bbt_i/quant_bbt, 2), round(media_bbt_n/quant_bbt, 2)))
    print('Friends:              {}(IMDB)  {}(Netflix)'.format(round(media_fr_i/quant_fr, 2), round(media_fr_n/quant_fr, 2)))
    
    



