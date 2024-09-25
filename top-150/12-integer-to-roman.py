class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        my_num = num
        ones = my_num % 10
        my_num = int((my_num - ones) / 10)

        tens = my_num % 10
        my_num = int((my_num - tens) / 10)

        hundreds = my_num % 10
        my_num = int((my_num - hundreds) / 10)

        thousands = my_num % 10

        s = ''
        s += thousands * 'M'

        if hundreds == 9:
            s += 'CM'
        elif 5 <= hundreds <= 8:
            s += 'D' + 'C' * (hundreds % 5)
        elif hundreds == 4:
            s += 'CD'
        else:
            s += 'C' * hundreds

        if tens == 9:
            s += 'XC'
        elif 5 <= tens <= 8:
            s += 'L' + 'X' * (tens % 5)
        elif tens == 4:
            s += 'XL'
        else:
            s += 'X' * tens

        if ones == 9:
            s += 'IX'
        elif 5 <= ones <= 8:
            s += 'V' + 'I' * (ones % 5)
        elif ones == 4:
            s += 'IV'
        else:
            s += 'I' * ones

        return s

print(Solution.intToRoman(Solution(), 3749))