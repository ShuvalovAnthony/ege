f = open("24/40740/40740.txt").read()


# max_len = 0

# for word in f.split("A"):
#     if word.count("E") >= 3:
#         max_len = max(max_len, len(word))

# print(max_len)



print(
    max(
        [
            len(word) for word in f.split("A") if word.count("E") >= 3
        ]
    )
)