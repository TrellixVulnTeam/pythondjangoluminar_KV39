n=int(input('enter the value of  n :'))
first_num=0
second_num=1
sum=0
count=1
print("fibonacci series:",end=" ")
while (count <=n):
    print(sum,end='')
    count+=1
    first_num=second_num
    second_num=sum
    sum=first_num+second_num