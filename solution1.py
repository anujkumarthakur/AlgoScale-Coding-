'''Problem-1:
    Given an array of integers, return indices of the two numbers such that they add up to a
    specific target. You may assume that each input would have exactly one solution, and
    you may not use the same element twice. '''

def AddTwo(arr, target):
    n = len(arr)
    #bubble sort
    for i in range(0, n):
        for j in range(0, n-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    #logic
    for i in range(0,n):
        for j in range(i,n):
            if(arr[j] + arr[j+1] == target):
                print([j,j+1])
            else:
                print("Invalied No are Exists")
#Driver Code
if __name__ == "__main__":
    n = int(input("How many number do you want to store in array :"))
    target = int(input("Enter a target value :"))
    arr = []
    for i in range(n):
        inp = int(input())
        arr.append(inp)
    AddTwo(arr, target)
