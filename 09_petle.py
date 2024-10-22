"""
for

while

else
break
continue



"""

text = "Ala ma kota"

for sign in text:
    if sign == " ":
        break
    print(sign)
else:
    print("To jest zawartosc else")

print(sign)

i = 0
while i < len(text):
    if text[i] == " ":
        break
    print(text[i])
    i += 1

for sign in text:
    print(sign)
#
#
# liczby = []
# # for i in range(1000000):
# while True:
#     l = input("Podaj liczbę lub daj enter by zakonczyc: ")
#     if not l:
#         break
#     liczby.append(int(l))

# ctrl + /