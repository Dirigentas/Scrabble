# turimų raidzių įrašymas
a = ''
temp = ""

# Ši sub-programa paskaičiuoja kiek taškų vertas žodis
def get_value(word):
    letter_value = ({'a': 1, 'ą': 8, 'b': 2, 'c': 10, 'č': 8, 'd': 2,
                     'e': 1, 'ę': 10, 'ė': 4, 'f': 10, 'g': 4, 'h': 10,
                     'i': 1, 'į': 8, 'y': 5, 'j': 4, 'k': 1, 'l': 2,
                     'm': 2, 'n': 1, 'o': 1, 'p': 3, 'r': 1, 'š': 5, 's': 1,
                     't': 1, 'u': 1, 'ų': 6, 'ū': 8, 'v': 4, 'z': 10, 'ž': 6})
    count = 0
    for adding in word:
        count += letter_value[adding]
    return count


raides = (input("Įrašyti turimas raides (7 raidės be tarpų): ")).lower()
# meta klaidą įrašius ne raides ir ne 7 simbolius
if not raides.isalpha() or len(raides) != 7:
    print('Klaida, prašau įrašyti 7 abėsėlės raides')
    quit()
print('4-7 raidžių žodžiai:')
# importuojami visi lietuviški žodžiai
with open("./LT zodiai.txt", encoding="UTF-8") as data_file:
    for line in data_file:
# /n nuėmimas
        line = line.rstrip()
# žodžio paieška duomenų bazėje
        if sorted(line) == sorted(raides):
            a += line
            # panaikina pasikartojančius žodžius ir parašo kiek taškų vertas žodis.
            if temp != line:
                print(f'{line} {get_value(line)} taškai')
            temp = line
# nuima 1 raidę
        raides = sorted(raides)
        for c in range(7):
            removed = raides.pop(c)
            if sorted(line) == raides:
                a += line
                # panaikina pasikartojančius žodžius ir parašo kiek taškų vertas žodis.
                if temp != line:
                    print(f'{line} {get_value(line)} taškai')
                temp = line
# nuima dar vieną raidę, tai jau 2 nuimtos
            for d in range(6):
                removed2 = raides.pop(d)
                if sorted(line) == raides:
                    a += line
                    # panaikina pasikartojančius žodžius ir parašo kiek taškų vertas žodis.
                    if temp != line:
                        print(f'{line} {get_value(line)} taškai')
                    temp = line
# nuima dar vieną raidę, tai jau 3 nuimtos
                for e in range(5):
                    removed3 = raides.pop(e)
                    if sorted(line) == raides:
                        a += line
                        # panaikina pasikartojančius žodžius ir parašo kiek taškų vertas žodis.
                        if temp != line:
                            print(f'{line} {get_value(line)} taškai')
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

  3. kad išmestų klaidą įrašius ne 7 raides        +

  4. kad butu nesvarbu irasyti didz ar mazasias raides  (Dovis)

  5. surasti kodo klaidą kodėl dubliuoja žodius    (Dovis)
        (testuoti su 'aeoėbjn')

  6. reikia, kad parasytu tasku skaiciu salia zodzio
    6.1 surusiuotu rastus žodžius pagal sudėtingumą

  7. pridėti funkcionalumą, kad būtų galima įrašyti simbolį, kuris reiškia bet kokią lietuviškos abėcėlės raidę


    '''
