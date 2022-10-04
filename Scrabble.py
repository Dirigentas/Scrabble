# turimų raidzių įrašymas
print("Įrašyti turimas raides (tik mažosios raidės:)")
raides=(input())
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

    kaip ieškoti 6 raidžių žodžių jei 7 nėra.
        pradžioj vieną raidę atmeta ir ieško
        jei nerandu, tuomet 2 raides atmetu ir ieškau žodžio

    reikia, kad parasytu, kad nerado jei neranda

    reikia, kad surusiuotu rastus žodžius pagal sudėtingumą

    

    '''
