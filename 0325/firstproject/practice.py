import random

list = []
ran_num = random.randint(0,45)

for i in range(6):
     while ran_num in list:
         ran_num = random.randint(1, 45)
     list.append(ran_num)

list.sort()
print(list)
    