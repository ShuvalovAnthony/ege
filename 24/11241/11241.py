f = open("24/11241/24_11241.txt").read()

f = (f
     .replace("A", " ")
     .replace("B", " ")
     .replace("C", " ")
     .replace("D", " "))


print(
    max(
        [len(i) for i in f.split()]
    )
)