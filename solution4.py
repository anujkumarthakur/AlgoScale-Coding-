'''
Q4. MOUNTAINEER ARRAY --Problem:
        Given an array A of integers, return true if and only if it is a valid mountain array.
        Recall that A is a mountain array if and only if:
'''

def MOUNT(arr):
    length = len(arr)
    if length < 3:
        return False
    n =2
    for i in range(length):
        start = arr[i] - arr[i-1]
        end = arr[i+1] - arr[i]
        if start > 0 and end <0:
            n = n-1
        if start < 0 and end > 0 or start ==0 or end == 0:
            return False
    return n == 1

if __name__ == "__main__":
    x = int(input("How many Number do you want :"))
    arr = []
    for i in range(x):
        inp = int(input())
        arr.append(inp)
    y = MOUNT(arr)
    print(y)
