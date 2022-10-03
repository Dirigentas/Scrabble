# turimų raidzių įrašymas
i=1
b=''
while i <8:
    zodis=input()
    i+=1
    b+=zodis
# importuojami visi lietuviški žodžiai
with open("C:\\Users\\Aras\\Desktop\\Python\\LT zodiai 2.txt") as data_file:
    for line in data_file:
# paskutinio žodžio paskutinės raidės nenutrynimas
        if line.isalpha()==False:
# /n nuėmimas
            line = line[:-1]
# pavertimas į list'us
        line = list(line)
# žodžio paieška duomenų bazėje
        print(line)
        if sorted(line) == sorted(list(b)):
            print(''.join(line))


'''
Dar reikia:

    pagrindin4 problema, randa klaidą duomenyse, kurią dar nežinau kaip ištaisyti

    kaip ieškoti 6 raidžių žodžių jei 7 nėra?
        pradžioj vieną raidę atmetu ir ieškau
        jei nerandu, tuomet 2 raides atmetu ir ieškau žodžio

    klausimas ka daryti jei randa kelis zodius???
        nuodoti pirmą
        išrašyti visus
        surašyti taisykles, kad naudotų sudėtingiausią

    ištrinti vietovardžius (kas iš didž raidės)
        nors ir sugalvojau būdą, nesuveikė, testuoti kada vėl
    '''
