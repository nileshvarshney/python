nums = [0,0,1,1,1,2,2,3,3,4]
# for i in range(len(nums)):
#     try:
#         if nums[i-1] == nums[i]:
#             del nums[i-1]
#     except IndexError:
#         pass

# print(nums)
def unique_list(nums):
    return list(set(nums))

print(unique_list(nums))