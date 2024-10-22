
try:
    f = open("cwiczenie_01.py")
    1/0
except ZeroDivisionError as e:
    print(e)
    print("wykonuje sie except")
except ValueError:
    print("Value error... ")
except Exception as e:
    ...
finally:
    print("wykonuje sie finally")
    f.close()


with open("cwiczenie_01.py") as f:
    print(f.read())

print("tu jestem juz po context manager")
