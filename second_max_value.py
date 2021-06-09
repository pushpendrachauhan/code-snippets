import math

def get_second_max(arr):
	if arr is None:
		return -1
	max_value=math.inf
	second_max_value=math.inf
	i=0
	while i<len(arr):
		try:
			current_value=int(arr[i])
		except ValueError as e:
			return -1

		if max_value == math.inf:
			max_value=current_value
		elif current_value>max_value:
			second_max_value=max_value
			max_value=current_value
		else:
			if second_max_value == math.inf and current_value != max_value:
				second_max_value=current_value
			else:
				if current_value>second_max_value and current_value != max_value:
					second_max_value=current_value

		i+=1
	if (max_value == math.inf or second_max_value == math.inf ):
		return -1
	else:
		return second_max_value


if __name__=="__main__":
	print (get_second_max(["1","2","3","4"]))
