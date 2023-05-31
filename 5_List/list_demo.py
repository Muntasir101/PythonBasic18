numbers = [1,20,11,50,70,88,90,2]

length = len(numbers)
print('length:', length)

first_element = numbers[0]
print('First element:', first_element)

second_element = numbers[1]
print('Second element:', second_element)

last_element_index = length - 1
print('Last element:', numbers[last_element_index])

# adding element to the end of the list
numbers.append(85)
print("After adding element to last:", numbers)

# adding element to any index in the list
numbers.insert(0, 200)
print("After adding element in 0 index:", numbers)

length = len(numbers)
print('length:', length)

# removing element from the end of the list
numbers.pop()
print('after pop element:', numbers)

# modifying element
numbers[0] = 500
print('after modify element:', numbers)

# sorting list
sorting = sorted(numbers)
print('after sort list:', sorting)

# descending sorting
numbers.sort(reverse=True)
print('after descending sort list:', numbers)


