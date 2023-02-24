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
    
    
def longest_run_recursive(mylist, key):
	def longest_run_recursive_helper(mylist, key, Result):
		if len(mylist) == 0:
			return Result(0,0,0,False)
		mid = len(mylist) // 2
		left = mylist[:mid]
		right = mylist[mid:]
		#print("list: {} \nleft: {} \nright: {}".format(mylist, left, right))
		if len(mylist) == 2:
			if left and left[0] == key:
				Result.left_size += 1
			#	print("longest size (L) {}\n".format(Result.left_size))
			if right and right[0] == key:
				Result.right_size += 1
			#	print("longest size (R) {}\n".format(Result.right_size))
			return Result
		if len(mylist) == 1:
			if mylist[0] == key:
				Result.right_size += 1
			#	print("longest size (1) {}\n".format(Result.right_size))
			return Result
		else:
		#	print("recurring\n")
			left_size = longest_run_recursive_helper(left,key,Result).left_size
			right_size = longest_run_recursive_helper(right, key, Result).right_size
		if left and left[-1] == key and right and right[0] == key:
		#	print("left size: {} right size: {}".format(Result.left_size, Result.right_size))
			Result.longest_size = left_size + right_size
		else:
			Result.longest_size = max(left_size, right_size)
		if Result.longest_size == len(mylist):
			Result.is_entire_range = True
		else:
				Result.is_entire_range = False
		return Result
	mid = len(mylist) // 2
	left = mylist[:mid]
	right = mylist[mid:]
	left_result = longest_run_recursive_helper(left, key, Result(0,0,0,False))
	right_result = longest_run_recursive_helper(right, key, Result(0,0,0,False))
	if left_result.is_entire_range == True and right_result.is_entire_range == True:
		is_entire_range = True
	else:
		is_entire_range = False
	if left[-1] == right[0]:
		return Result(left_result.longest_size, right_result.longest_size, left_result.longest_size + right_result.longest_size, is_entire_range)
	else:
		return Result(left_result.longest_size, right_result.longest_size, max(left_result.longest_size, right_result.longest_size), is_entire_range)
	
	
		
print(longest_run_recursive([1,12,12,12,1,12], 12))
## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run_recursive([1,12,12,12,1,12], 12).longest_size == 3

