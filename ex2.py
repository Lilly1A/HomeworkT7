"""Scrieți un program care generează un număr aleatoriu între 1 și 100 și
permite utilizatorului să ghicească numărul. Programul ar trebui să furnizeze
feedback ("mai mare" sau "mai mic") până când utilizatorul ghicește numărul corect. Programul ar trebui,
de asemenea, să țină evidența numărului de încercări necesare pentru ca utilizatorul să ghicească corect."""

import random
numar=random.randint(1,10)
print(numar)
i=int(input('Introdu numarul '))
while i!=numar:
    print('Mai incearca odata')
    i=int(input('Introdu numarul '))

if i==numar:
    print('Game over')
