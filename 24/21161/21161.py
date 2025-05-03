from re import findall


f = open("ege/24/21161/24_21161.txt").read()


pattern = r'([ABC][abc]*(?: [ABCabc][abc]*)*\.)'

words = findall(pattern, f)
print([i for i in words if len(i) > 20])
# print(words)
print(max([len(i) for i in words]))



# sposob 2
# sentences = f.split(".")

# def check(sentence: str):
#     if not sentence: return False
#     if sentence[0] == ' ': return False
#     if sentence[0] not in "ABC": return False
#     if sentence[-1] == ' ': return False
#     if "  " in sentence: return False
#     for word in sentence.split():
#         for letter in "ABC":
#             if letter in word[1:]: return False

#     return True

# max_len = 0

# for sentence in sentences:
#     if check(sentence):
#         max_len = max(max_len, len(sentence) + 2)

# print(max_len)
