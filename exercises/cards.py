suits = ['spades', 'hearts', 'diamonds', 'clubs']
faces = ['jack', 'queen', 'king']
k = 0

while k < 4:
    print(f"ace of {suits[k]}")
    for i in range(2, 11):
        print(f"{i} of {suits[k]}")
    for i in faces:
        print(f"{i} of {suits[k]}")
    k += 1