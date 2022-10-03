# turimų raidzių įrašymas
raides=(input())
#print(sorted(list(raides)))
# importuojami visi lietuviški žodžiai
with open("C:\\Users\\Aras\\Desktop\\Programavimas\\Python\\Scrabble\\LT zodiai.txt", encoding="UTF-8") as data_file:
    for line in data_file:
# /n nuėmimas
        line = line.rstrip()
# pavertimas į list'us
        line = list(line)
# žodžio paieška duomenų bazėje
        #hprint(line)
        if sorted(line) == sorted(list(raides)):
            print(line)


'''
Dar reikia:

    kaip ieškoti 6 raidžių žodžių jei 7 nėra?
        pradžioj vieną raidę atmetu ir ieškau
        jei nerandu, tuomet 2 raides atmetu ir ieškau žodžio
    
    reikia prarasyti ka reikia irasyti

    reikia, kad parasytiu, kad nerado jei neranda

    

    '''
