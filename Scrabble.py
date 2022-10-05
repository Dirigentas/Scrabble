# turimų raidzių įrašymas
a = ''
raides=(input("Įrašyti turimas raides (tik mažosios raidės):"))
# importuojami visi lietuviški žodžiai
with open("C:\\Users\\Aras\\Desktop\\Programavimas\\Python\\Scrabble\\LT zodiai.txt", encoding="UTF-8") as data_file:
    for line in data_file:
# /n nuėmimas
        line = line.rstrip()
# žodžio paieška duomenų bazėje
        if sorted(list(line)) == sorted(list(raides)):
            a += line
            print(line)
        if sorted(list(line))==sorted(list(raides[1:])):
            print(line)
        '''if sorted(list(line))==sorted(list(raides[1:])):
            print(line)
        if sorted(list(line))==sorted(list(raides[1:])):
            print(line)
        if sorted(list(line))==sorted(list(raides[1:])):
            print(line)
        if sorted(list(line))==sorted(list(raides[1:])):
            print(line)
        if sorted(list(line))==sorted(list(raides[1:])):
            print(line)
        if sorted(list(line))==sorted(list(raides[1:])):
            print(line)'''
        





print('Su tokiomis raidėmis žodžių nėra' if not a.isalpha() else '!!!')

        
        




'''
Dar reikia:

  1.  reikia, kad parasytu, kad nerado jei neranda  +

  2.  Surasti visus galimus žodžius ir su mažiau raidžių

  3.  reikia, kad surusiuotu rastus žodžius pagal sudėtingumą

    

    '''
