# Dividir e conquistar
def merge_sort(array):
	if len(array) <= 1:
		return array

	mid = len(array) // 2
	leftHalf = array[:mid]
	rightHalf = array[mid:]

	sortedLeft = merge_sort(leftHalf)
	sortedRight = merge_sort(rightHalf)

	return merge(sortedLeft, sortedRight)

def merge(left, right):
	result = []
	i = j = 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else: 
			result.append(right[j])
			j += 1

	result.extend(left[i:])
	result.extend(right[j:])

	return result

array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
merge_sort(array)
print(array)