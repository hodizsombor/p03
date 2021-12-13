#Írj programot, mely beolvas két egész számot, és kiírja a képernyőre a nagyobbikat!

szam = int(input('adj meg egy számot. '))
szamm = int(input('adj meg még egy számot. '))

if szam == szamm:
  print('a két szám egyellő')
elif szam < szamm:
  print('a második szám nagyobb')
else:
  print('az első szám nagyobb')