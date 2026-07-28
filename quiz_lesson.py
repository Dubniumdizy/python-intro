'''
Skapa en while loop som är True
Fråga användaren om namn, ålder, intresse - sparas i en dict()
Printa åldern om 5 år, om negativ ålder säg till är fel, om över 100 säg ett medeleande
Printa sammanfaante slutbrev med all info
Om användern skriver exit, avsluta

while True:
    name = input("What is your name")
    age = input("What is your age")
    interest = input("What is your interest")
    print("If you want to exit, write 'exit'")
'''


lst = ['katt', 'hund', 'häst', 'får', 'bird']

for item in lst:
    print(item)

idx = 0
while idx < len(lst):
    print(lst[idx]) # print(idx)
    idx = idx + 1