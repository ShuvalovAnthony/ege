num = 4**36 + 3*4**20 + 4**15 + 2*4**7 + 49


answ = set(hex(num)[2::]) # str

print(len(answ))