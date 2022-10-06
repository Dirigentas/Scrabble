# turimų raidzių įrašymas
a = ''
raides=(input("Įrašyti turimas raides (tik mažosios raidės): "))
# importuojami visi lietuviški žodžiai
with open("C:\\Users\\Aras\\Desktop\\Programavimas\\Python\\Scrabble\\LT zodiai.txt", encoding="UTF-8") as data_file:
    for line in data_file:
# /n nuėmimas
        line = line.rstrip()
# žodžio paieška duomenų bazėje
        if sorted(line) == sorted(raides):
            a += line
            print(line)
# nuima vieną raidę
        raides = sorted(raides)
        for c in range(4): #čia galiu paskui pririšti prie įrašyto raižių len
            removed = raides.pop(c)
            if sorted(line) == raides:
                print (line)
            raides.append(removed)
            raides=sorted(raides)
# nuima dvi raides
        for c in range(4):
            

        





print('Su tokiomis raidėmis žodžių nėra' if not a.isalpha() else '!!!')

        
        




'''
Dar reikia:

  1.  reikia, kad parasytu, kad nerado jei neranda  +

  2.  Surasti visus galimus žodžius ir su mažiau raidžių

  3.  reikia, kad surusiuotu rastus žodžius pagal sudėtingumą

    

    '''
