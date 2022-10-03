'''with open("C:\\Users\\Aras\\Desktop\\Programavimas\\Python\\Scrabble\\LT zodiai 2.txt") as data_file:
    print(data_file)
    for line in data_file:
        print(line)'''


a = open('LT zodiai 2.txt', encoding="UTF-8") 
print(a)
for line in a:
    line = line.rstrip() #panaikina ne printable objects
    print(line)