from __future__ import division

remnant_hash = {}
class Solution:
    # @return a string
    def get_decimals(self, result, number, remnant, denominator): # here remnant must be smaller than denominator
        print "remnant is:", remnant
        if remnant in remnant_hash.keys():
            i = remnant_hash[remnant]
            result = result[:i] + "(" + result[i:] + ")"
            return result
        else:
            print "enter here"
            remnant = 10 * remnant
            quotient = remnant // denominator
            remnant = remnant % denominator
            result = result + str(quotient)
            remnant_hash[remnant] = number
            result = self.get_decimals(result, number+1, remnant, denominator)
            print "The result is:", result

    def fractionToDecimal(self, numerator, denominator):

        result = ""
        quotient = numerator // denominator
        remnant = numerator % denominator
        result = str(quotient) + "."
        result = result + self.get_decimals("", 1, remnant, denominator)
        return result




if __name__ == "__main__":
    solution = Solution()
    result = solution.fractionToDecimal(8, 11)
    print result




