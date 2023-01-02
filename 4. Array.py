#1. Write a function to add integer values of an array
nums = [5, 6, 7, 8]
nums.append(9)

#2. Write a function to calculate the average value of an array of integers
def average( a , n ):
    s = 0
    for i in range(n):
        s += a[i]
        return s/n
arr = [1, 2, 3, 4, 5]
n = len(arr)
print(average(arr, n))


#3. Write a program to find the index of an array element
nums = [5, 6, 7, 8]
ins = nums.index(5)
print(ins)

#4. Write a function to test if array contains a specific value
nums = [5, 6, 7, 8]
a = int(input("enter number to check:"))
if a in nums:
    print('Available')
else:
    print("not available")


#5. Write a function to remove a specific element from an array
nums = [5, 6, 7, 8]
nums.remove(5)
print(nums)


#6. Write a function to copy an array to another array
nums = [5, 6, 7, 8]
nums1 = nums.copy()
print(nums1)


#7. Write a function to insert an element at a specific position in the array
nums = [5, 6, 7, 8]
nums.insert(3, 10)
print(nums)


#8. Write a function to find the minimum and maximum value of an array
nums = [5, 6, 7, 8]
a = min(nums)
b = max(nums)
print(a)
print(b)


#9. Write a function to reverse an array of integer values
nums = [5, 6, 7, 8]
nums.reverse()
print(nums)


#10. Write a function to find the duplicate values of an array
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        if(nums[i] == nums[j]):    
            print(nums[j]);    


#11. Write a program to find the common values between two arrays   
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums1 = [5, 6, 7, 8]
result = []
for i in range(len(nums)):
    for j in range(len(nums1)):
        if nums[i]==nums1[j]:
            result.append(nums[i])
print(result)


#12. Write a method to remove duplicate elements from an array
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []
for i in range(len(nums)):
    if nums[i] not in result:
        result.append(nums[i])
print(result)

#13. Write a method to find the second largest number in an array
nums = [5, 6, 7, 8]
nums.sort()
print(nums[-2])
 

#14. Write a method to find the second largest number in an array
nums = [5, 6, 7, 8]
nums.sort()
print(nums[-2])


#15. Write a method to find number of even number and odd numbers in an array
nums = [5, 6, 7, 8]
odd = []
even = []
for i in range(len(nums)):
    if(nums[i]%2) == 0:
        odd.append(nums[i])
    else:
        even.append(nums[i])
print(odd)
print(even)


#16. Write a function to get the difference of largest and smallest value
nums = [5, 6, 7, 8]
a = min(nums)
b = max(nums)
c = b - a
print('difference of largest and smallest value is', c)


#17. Write a method to verify if the array contains two specified elements(12,23)
nums = [12, 23, 5, 6, 7, 8]
a = [12, 23]
for i in range(len(nums)):
    for j in range(len(a)):
        if(a[j] != nums[i]):
            print("not available here")
        else:
            print("available here")

#18. Write a program to remove the duplicate elements and return the new array
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []
for i in range(len(nums)):
    if nums[i] not in result:
        result.append(nums[i])
print(result)