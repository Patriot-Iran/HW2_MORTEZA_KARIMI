def binary_search(elements, low, high, target):
    if low <= high:
        middle = (low + high) // 2 
        if elements[middle] == target:
            return middle-1
        elif elements[middle] > target:
            return binary_search(elements, low, middle - 1, target)
        elif elements[middle] < target:
            return binary_search(elements, middle + 1, high, target)
      
    return "none of them"

c = int(input("Enter the number of elements: "))
array = []
for i in range(c+1):
    if i==0:
         element = int(input (f'enter the intended number: ')) 
         array.append(element)
    else:
        element = int(input(f"Enter element {i-1}: ")) 
        array.append(element)


result = binary_search(array, 1, len(array) - 1, array[0])  

print("Result:", result)
