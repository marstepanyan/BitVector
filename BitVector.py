import math


class BitVector:
    def __init__(self, length):
        self._length = length
        self._lst = [0] * math.ceil(length/64)

    def set(self, set_idx):
        if set_idx > 64:
            idx = set_idx - (set_idx//64)*64 - 1
            number_index = set_idx//64

        else:
            number_index = 0
            idx = set_idx

        self._lst[number_index] += 2 ** idx

        return self._lst

    def reset(self, reset_idx):
        if reset_idx > 64:
            idx = reset_idx - (reset_idx//64)*64 - 1
            number_index = reset_idx//64

        else:
            number_index = 0
            idx = reset_idx

        if self._lst[number_index] > 2 ** idx:
            self._lst[number_index] -= 2 ** idx
        else:
            return print(f'index {reset_idx} was not 1')

        return self._lst

    def __str__(self):
        return str(self._lst[::-1])


b = BitVector(200)
print(b)
print()
b.set(73)
b.set(2)
b.set(198)
b.set(0)
print(b)
b.reset(0)
b.reset(3)
b.reset(70)
b.reset(73)
print()
print('Final vector b:', b)
