class BitVector:
    def __init__(self, length):
        self._length = length
        self._lst = [0] * ((length // 32) + 1)

    def set(self, set_idx):
        if set_idx < 32:
            number_index = 0
            idx = set_idx

        else:
            idx = set_idx - ((set_idx // 32) * 32)
            number_index = set_idx // 32

        self._lst[number_index] += 2 ** idx

        print(f'Vector after setting 1 in index {set_idx}:', self._lst[::-1])
        return self._lst[::-1]

    def reset(self, reset_idx):
        if reset_idx < 32:
            number_index = 0
            idx = reset_idx

        else:
            idx = reset_idx - ((reset_idx // 32) * 32)
            number_index = reset_idx // 32

        if self._lst[number_index] & 2 ** idx:
            self._lst[number_index] -= 2 ** idx
        else:
            return print(f'Vector after resetting 1 in index {reset_idx} is the same cause index {reset_idx} was not 1')

        print(f'Vector after resetting 1 in index {reset_idx}:', self._lst[::-1])
        return self._lst[::-1]

    def __str__(self):
        return str(self._lst[::-1])


b = BitVector(100)
print('Vector before changes: ', b)
print()
b.set(73)
b.reset(72)
b.set(72)
b.reset(73)
b.set(5)
b.reset(0)
b.set(32)
print()
print('Final vector b:', b)
