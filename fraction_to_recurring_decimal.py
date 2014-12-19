from __future__ import division

remnant_hash = {}
class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        remnant_hash = {}
        count = 0
        result = ""
        result_integar = ""
        result_decimal = ""
        sign = ""
        if numerator < 0 and denominator > 0:
            sign = "-"
            numerator = 0 - numerator
        elif numerator > 0 and denominator < 0:
            sign = "-"
            denominator = 0 - denominator
        elif numerator < 0 and denominator < 0:
            numerator = 0 - numerator
            denominator = 0 - denominator
        else:
            pass
        quotient = numerator // denominator
        remnant = numerator % denominator
        if remnant == 0:
            result = sign + str(quotient)
        else:
            result_integar = str(quotient) + "."
            result_decimal = ""
            while remnant not in remnant_hash.keys():
                remnant_hash[remnant] = count
                count += 1
                quotient = 10 * remnant // denominator
                remnant = 10 * remnant % denominator
                result_decimal = result_decimal + str(quotient)
                if remnant == 0: # which means that there is no recurring decimals
                    break
            if remnant == 0:
                result = sign + result_integar + result_decimal
            else:
                num = remnant_hash[remnant]
                result = sign + result_integar + result_decimal[:num] + "(" + result_decimal[num:] + ")"
        return result

if __name__ == "__main__":
    solution = Solution()
    result = solution.fractionToDecimal(7, -12)
    print result




