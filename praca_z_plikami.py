
# dane = [[x, x**2, x**3] for x in range(100)]

# with open("data.txt", "w") as f:
#     for wiersz in dane:
#         f.write(f"{wiersz[0]},{wiersz[1]},{wiersz[2]}\n")
#
#


with open("dane/data.txt") as f:
    for line in f:
        a, b, c = line.strip().split(",")
        print(int(a) + int(b) + int(c))


