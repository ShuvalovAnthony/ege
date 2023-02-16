from typing import List

def fano_codes(n: int) -> List[str]:
    symbols = [chr(ord('A') + i) for i in range(n)]
    freq = [1] * n

    def generate_fano_codes(start: int, end: int) -> List[str]:
        if end - start == 1:
            return [symbols[start]]

        total_freq = sum(freq[start:end])
        left_freq = 0
        min_diff = float('inf')
        split_point = -1

        for i in range(start, end):
            left_freq += freq[i]
            right_freq = total_freq - left_freq
            diff = abs(left_freq - right_freq)

            if diff < min_diff:
                min_diff = diff
                split_point = i

        left_codes = [code + '0' for code in generate_fano_codes(start, split_point)]
        right_codes = [code + '1' for code in generate_fano_codes(split_point, end)]
        return left_codes + right_codes

    return generate_fano_codes(0, n)


print(fano_codes(1))