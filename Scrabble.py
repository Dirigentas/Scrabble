# turimų raidzių įrašymas
a = ''
raides=(input("Įrašyti turimas raides (7 mažosios raidės be tarpų): "))
print('4-7 raidžių žodžiai:')
# importuojami visi lietuviški žodžiai
with open("C:\\Users\\Aras\\Desktop\\Programavimas\\Python\\Scrabble\\LT zodiai.txt", encoding="UTF-8") as data_file:
    for line in data_file:
# /n nuėmimas
        line = line.rstrip()
# žodžio paieška duomenų bazėje
        if sorted(line) == sorted(raides):
            a += line
            print(line)
# nuima 1 raidę
        raides = sorted(raides)
        for c in range(7): #čia galiu paskui pririšti prie įrašyto raižių len
            removed = raides.pop(c)
            if sorted(line) == raides:
                print (line)
# nuima dar vieną raides, tai jau 2 nuimtos
            for d in range(6): #čia galiu paskui pririšti prie įrašyto raižių len
                removed2 = raides.pop(d)
                if sorted(line) == raides:
                    print (line)
# nuima dar vieną raides, tai jau 3 nuimtos
                for e in range(5): #čia galiu paskui pririšti prie įrašyto raižių len
                    removed3 = raides.pop(e)
                    if sorted(line) == raides:
                        print (line)
                    raides.append(removed3)
                    raides = sorted(raides)
                raides.append(removed2)
                raides = sorted(raides)
            raides.append(removed)
            raides=sorted(raides)
print('Su išvardintomis raidėmis žodžių nerasta' if not a.isalpha() else '!!!')

        
        


'''
Dar reikia:

  1.  reikia, kad parasytu, kad nerado jei neranda  +

  2.  Surasti visus galimus žodžius su 4-7 raidėmis +

  3.  reikia, kad surusiuotu rastus žodžius pagal sudėtingumą

  4. kad išmestų klaidą įrašius ne 7 raides

  5. surasti klodo klaidą kodėl dubliuoja žodius
        (testuoti su 'aeoėbjn')


    '''
