class Soltution():
    def twoSum(self, nums, target):
        for i ,n in enumerate(nums):
            remaining = target - n
            print(remaining)
            if remaining in nums[i+1:]:
                return [i, nums[i+1:].index(remaining) + i + 1]


if __name__ == "__main__":
    nums =  [2, 7, 11, 15]
    target = 9
    sol = Soltution()
    print(sol.twoSum(nums, target))