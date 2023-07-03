N = int(input())

sum = 0
for i in range(0, N):
    term = int(input())
    sum += ((term - term%10)/10)**(term % 10)
print(int(sum))
