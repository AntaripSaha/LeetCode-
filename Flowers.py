flowerbed = [0,0,1,0,0,0,1,0,0]
n = 4

for i in range(len(flowerbed)):
    first_slot = (i == 0) or (flowerbed[i-1]==0)
    last_slot = (i == len(flowerbed)-1) or (flowerbed[i+1]==0)
    print(first_slot)
    if n == 0:
        # print('True')
        exit()
    elif first_slot and flowerbed[i] == 0 and last_slot:
        flowerbed[i] = 1
        n -= 1

# print('False')

