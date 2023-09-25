#1.Write a function called linear_search_product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found.
def search(a, l, x):

    # Traversing the array 
    for i in range(l):
        if (a[i] == x):
            return i
    return -1

a = [10, 8, 6, 4, 2]
print("The given array is ", a)
x = 6
print("Element to be searched is ", x)
l = len(a)
ind = search(a, l, x)
if(ind == -1):
    print("Element Not Found")
else:
    print("Element is at index ", ind)