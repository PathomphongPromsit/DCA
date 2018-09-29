print("monthly")
ml = int(input())
print("day")
d = float(input())
print("X month")
m = int(input())

sum = ml
for i in range(m):
    for i in range(20):
        sum = sum*((100+d)/100)
        #print(sum)
    sum += ml
print(sum)