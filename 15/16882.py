def process_number(N):
    binary = bin(N)[2:].zfill(8)
    reversed_binary = binary.translate(str.maketrans('01', '10'))
    new_number = int(reversed_binary, 2)
    return new_number - N


def find_number(result):
    for N in range(256):
        if process_number(N) == result:
            return N
    return None

result = 111
N = find_number(result)
print(N)
