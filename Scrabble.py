# turimų raidzių įrašymas
a = ''
raides = (input("Įrašyti turimas raides (7 raidės be tarpų): ")).lower()
# meta klaidą įrašius ne raides ir ne 7 simbolius
if not raides.isalpha() or len(raides) != 7 :
    print('Klaida, prašau įrašyti 7 abėsėlės raides')
    quit()
temp = ""
print('4-7 raidžių žodžiai:')
# importuojami visi lietuviški žodžiai
with open("./LT zodiai.txt", encoding="UTF-8") as data_file:
    for line in data_file:
# /n nuėmimas
        line = line.rstrip()
# žodžio paieška duomenų bazėje
        if sorted(line) == sorted(raides):
            a += line
            # panaikina pasikartojančius žodžius
            if temp != line:
                print(line)
            temp = line
# nuima 1 raidę
        raides = sorted(raides)
        for c in range(7):
            removed = raides.pop(c)
            if sorted(line) == raides:
                a += line
                # panaikina pasikartojančius žodžius
                if temp != line:
                    print(line)
                temp = line
# nuima dar vieną raidę, tai jau 2 nuimtos
            for d in range(6):
                removed2 = raides.pop(d)
                if sorted(line) == raides:
                    a += line
                    # panaikina pasikartojančius žodžius
                    if temp != line:
                        print(line)
                    temp = line
# nuima dar vieną raidę, tai jau 3 nuimtos
                for e in range(5):
                    removed3 = raides.pop(e)
                    if sorted(line) == raides:
                        a += line
                        # panaikina pasikartojančius žodžius
                        if temp != line:
                            print(line)
                        temp = line
                    raides.append(removed3)
                    raides = sorted(raides)
                raides.append(removed2)
                raides = sorted(raides)
            raides.append(removed)
            raides = sorted(raides)
print('Su išvardintomis raidėmis žodžių nerasta' if not a.isalpha() else '!!!')



'''
Dar reikia:

  1.  reikia, kad parasytu, kad nerado jei neranda  +

  2.  Surasti visus galimus žodžius su 4-7 raidėmis +

  3. reikia, kad parasytu tasku skaiciu salia zodzio
    3.1 surusiuotu rastus žodžius pagal sudėtingumą

  4. kad išmestų klaidą įrašius ne 7 raides        +

  5. kad butu nesvarbu irasyti didz ar mazasias raides  (Dovis)

  6. surasti kodo klaidą kodėl dubliuoja žodius    (Dovis)
        (testuoti su 'aeoėbjn')


    '''
