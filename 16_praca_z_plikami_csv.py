"""

comma separated value

a,b,c
1,2,3
2,3,4


a;b;c
1;2;3
2;3;4

a,b,c
1,ala,3
2,"a,b",4


"""

with open("dane/dane.csv") as f:
    for line in f:
        print(line.split(","))

import csv

with open("dane/dane2.csv") as f:
     reader = csv.reader(f, delimiter=";", quotechar="'")
     for row in reader:
         print(row)

with open("dane/dane2.csv") as f:
    reader = csv.DictReader(f, delimiter=";", quotechar="'")
    for row in reader:
        print(row)


dane = [[1, 2, 3], [4,5,6]]

with open("dane/dane3.csv", "w") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerows(["a", "b", "c"])
    for row in dane:
        writer.writerow(row)


dane = [{"a": 100, "b": 200}, {"a": 101, "b": 2022}]

with open("dane/dane3.csv", "w") as f:
    writer = csv.DictWriter(f, delimiter=";", fieldnames=["a", "b",])
    writer.writeheader()
    for row in dane:
        writer.writerow(row)


