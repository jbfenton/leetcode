class Solution:
    def reverse(self, x: int) -> int:
        upper_lim = (2 ** 31) - 1
        lower_lim = -2 ** 31

        if x < 0:
            new_int = 0 - int(str(x)[1:][::-1])
        else:
            new_int = int(str(x)[::-1])

        if lower_lim < new_int < upper_lim:
            return new_int

        return 0
