f = open('26/2580/26_2580.txt')

n, k = map(int, f.readline().split())

tmp_nums = []
max_stop = -1
# ищем максимум
for i in f:
    start, stop = map(int, i.split())
    start = max(start, k)
    tmp_nums.append([start, stop])
    if stop > max_stop: max_stop = stop

nums = []
times = set()
# 
for start, stop in tmp_nums:
    start = max(k, start)
    if stop == 0: stop = max_stop + 1
    nums.append([start, stop])
    times.add(start)
    times.add(stop)



nums = sorted(nums, key=lambda x: (x[0], x[1]))
times = sorted(list(times))
# записать все старты
# записать все стопы
# бежать по всем временам
# писать разницу сколько стартов минус стопов

# for i in times:
#     ...


max_streak = 0
max_threads = 0

tmp_threads = 0
tmp_streak = 0

print("SFD")

# for start, stop in nums: