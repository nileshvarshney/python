class Solution:
    def reverse(self, x:int):
        str_x = str(x)
        if str_x[0] in ['+','-']:
            sign = str_x[0]
            str_x = str_x[1:]
            rever = int(sign + str_x[len(str_x): 0: -1] + str_x[0])
        else:
            rever = int(str_x[len(str_x): 0: -1] + str_x[0] )
        
        if (abs(rever) > 2147483647):
            return 0
        else:
            return rever

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(1534236469))
