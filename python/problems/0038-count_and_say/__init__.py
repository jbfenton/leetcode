class Solution:
    def countAndSay(self, n: int) -> str:
        number_string = "1"
        counter = 1

        while counter < n:
            new_string = []

            current_char = number_string[0]
            char_count = 0

            for char in number_string:
                if char != current_char:
                    new_string.append(str(char_count) + current_char)
                    current_char = char
                    char_count = 1
                else:
                    char_count += 1
            else:
                new_string.append(str(char_count) + current_char)

            number_string = "".join(new_string)
            counter += 1

        return number_string
