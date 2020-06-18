class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        s_len = len(s)
        total = 0
        i = 0

        while i < s_len:
            if i + 1 < s_len:
                combined = "{}{}".format(s[i], s[i + 1])

                if combined in lookup:
                    total += lookup[combined]
                    i += 2
                    continue

            total += lookup[s[i]]
            i += 1

        return total
