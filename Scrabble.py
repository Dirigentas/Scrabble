# turimų raidzių įrašymas
a = ''
print("Įrašyti turimas raides (tik mažosios raidės):")
raides=(input())
# importuojami visi lietuviški žodžiai
with open("C:\\Users\\Aras\\Desktop\\Programavimas\\Python\\Scrabble\\LT zodiai.txt", encoding="UTF-8") as data_file:
    for line in data_file:
# /n nuėmimas
        line = line.rstrip()
# žodžio paieška duomenų bazėje
        if sorted(list(line)) == sorted(list(raides)):
            a += line
            print(line)
v = 'nera' if not a.isalpha() else ""
print(v)
'''if v == '':
    raides = '''
        
        




'''
Dar reikia:

  1.  reikia, kad parasytu, kad nerado jei neranda  +

  2.  ieškoti 6 raidžių žodžių jei 7 nėra.
        pradžioj vieną raidę atmeta ir ieško
        jei nerandu, tuomet 2 raides atmetu ir ieškau žodžio

  3.  reikia, kad surusiuotu rastus žodžius pagal sudėtingumą

    

    '''
