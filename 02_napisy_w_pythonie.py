
print("to jest napis")
print("to też 'jest' napis")
print('to też "jest" napis')
print("to też \"jest\" napis")

print("to jest napis\nz nowa\t linia")
print("to jest napis\\nz nowa\\t linia")
print(r"to jest napis\nz nowa\t linia")


print("""
1 linia 
2 linia
""")


print('''
1 linia 
2 linia
''')

x = (
    "ala"
    "ma"
    "kota"
)

x2 = "ala" \
    "ma" \
    "kota"

print(x)
print(x2)

napis1 = "Play"
napis2 = "ma ciekawą ofertę"
x = 10
print(napis1 + " " + napis2)

print("%s %s %.2f" % (napis1, napis2, 10))
print("%s %s %d" % (napis1, napis2, 10.2))

print("a {} {} {:.2f}"
      .format(napis1, napis2, x)
      .upper()
)

print(f"{napis1} {napis2} {x:.2f}")

print(napis1, napis2, sep="---")

# help(print)
# print(xxx)


print("=" * 80)

print("ala" == "ala")
print("pies" < "ries")


print(str(dir))
print(dir)

print("aax" in "aaax")

print("bbbbbbaaax".index("aax"))


for znak in "uhsfu9fdhbver":
    print(znak, end=":")


print()
#        012345678910
napis = "ala ma kota"

print(napis[0])

""
''