# turimų raidzių įrašymas
a = ''
temp = ""
line_scored = {}


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
            # panaikina pasikartojančius žodžius
            if temp != line:
                # Įdeda žodį ir žodžio vertę į lines_scored dictionary
                line_word = line
                score = get_value(line)
                line_scored[line_word] = score
            temp = line
# nuima 1 raidę
        raides = sorted(raides)
        for c in range(7):
            removed = raides.pop(c)
            if sorted(line) == raides:
                a += line
                # panaikina pasikartojančius žodžius
                if temp != line:
                    # Įdeda žodį ir žodžio vertę į lines_scored dictionary
                    line_word = line
                    score = get_value(line)
                    line_scored[line_word] = score
                temp = line
# nuima dar vieną raidę, tai jau 2 nuimtos
            for d in range(6):
                removed2 = raides.pop(d)
                if sorted(line) == raides:
                    a += line
                    # panaikina pasikartojančius žodžius
                    if temp != line:
                        # Įdeda žodį ir žodžio vertę į lines_scored dictionary
                        line_word = line
                        score = get_value(line)
                        line_scored[line_word] = score
                    temp = line
# nuima dar vieną raidę, tai jau 3 nuimtos
                for e in range(5):
                    removed3 = raides.pop(e)
                    if sorted(line) == raides:
                        a += line
                        # panaikina pasikartojančius žodžius ir parašo kiek taškų vertas žodis.
                        if temp != line:
                            # Adds found word to a line_scored dictionary
                            line_word = line
                            score = get_value(line)
                            line_scored[line_word] = score
                        temp = line
                    raides.append(removed3)
                    raides = sorted(raides)
                raides.append(removed2)
                raides = sorted(raides)
            raides.append(removed)
            raides = sorted(raides)
# Ištraukia žodžius iš line_scored norimu formatu, bet prieš tai juos visus surušiuoja nuo daugiausiai taškų surenkančio iki mažiausiai taškų surenkančio.
(print(*[str(k) + " " + str(v) + " taškai" for k, v in
         sorted(line_scored.items(), key=lambda x: x[1], reverse=True)], sep='\n'))
print('Su išvardintomis raidėmis žodžių nerasta' if not a.isalpha() else '!!!')
