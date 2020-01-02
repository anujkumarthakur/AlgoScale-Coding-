'''Q3. CAN PUT FLOWERS Problem:
            Suppose you have a long flowerbed in which some of the plots are planted and some are
            not. However, flowers cannot be planted in adjacent plots - they would compete for water
            and both would die.
            Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and
            1 means not empty), and a number n, return if n new flowers can be planted in it without
            violating the no-adjacent-flowers rule.
'''

def CanPutFlower(flowerbed, n):
    sum1 =0
    length = len(flowerbed)
    for i in range(length):
        if(flowerbed[i]==0 and ((i==length-1 and (length==1 or flowerbed[i-1]==0)) or (i==0 and flowerbed[i+1]==0) or (i>0 and i<length-1 and flowerbed[i-1]==0 and flowerbed[i+1]==0))):
            sum1 = sum1 + 1
            flowerbed[i] = i-1
    print(sum1>=n)
if __name__ == "__main__":
    sizeOfArray = int(input("how many number do you want:"))
    n = int(input("Enter a New Flower size : "))
    print("Number should be 0 and 1 formate")
    flowerbed = []
    for i in range(sizeOfArray):
        inp = int(input())
        flowerbed.append(inp)
    CanPutFlower(flowerbed,n)
            
