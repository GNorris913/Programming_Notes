### REVERSE INTEGER ###
class Solution:
    def reverse(self, x: int) -> int:
        negative = ''
        reverse = str(x)
        print(reverse)
        temp = []
        output = ""
        for letter in reverse:
            if letter == "-":
                negative = letter
            else:
                temp.append(letter)
        output = negative
        while temp:
            output = output + temp.pop()
        output = int(output)
        if output > math.pow(2, 31) or output < (math.pow(-2, 31) - 1):
            return 0
        return output