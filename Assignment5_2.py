'''
Docstring for Assignment5_2

Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

'''

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(original_list))

print(f"Original list is: {original_list}",)

firstfive = original_list[:5]
print(f"Extracted first five elements: {firstfive}")
reversed_list = firstfive[::-1]
print(f"Reversed extracted elements: {reversed_list}")
