"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.
def foo(x):
		if x <= 1:
			return x
		else:
			return foo(x-1) + foo(x-2)

def longest_run(mylist, key):
	longest = 0
	temp = 0
	for element in mylist:
		if element == key:
			temp+=1
		else:
			temp = 0
		if temp > longest:
			longest = temp
	return longest

		
				


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
# def longest_run_recursive(mylist, key, left_size, right_size):
# 	middle = (left_size + right_size) // 2
# 	if len(mylist) == 0: #base case 1
# 		return Result(0,0,0,False)
# 	left = mylist[:middle]
# 	right = mylist[middle:]
# 	left_size = longest_run_recursive(left, key, left_size, 0)
# 	right_size = longest_run_recursive(right, key, 0, right_size)
# 	if left[-1] == right[0]:
# 		longest_size = left_size + right_size + 1
# 	else:
# 		longest_size = max(left_size, right_size)
# 	if len(mylist) == longest_size:
# 		is_entire_range = True
# 	else:
# 		is_entire_range = False
# 	return Result(left_size, right_size, longest_size, is_entire_range)
		
# print(longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12, 0, 0))
# ## Feel free to add your own tests here.
# def test_longest_run():
#     assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

