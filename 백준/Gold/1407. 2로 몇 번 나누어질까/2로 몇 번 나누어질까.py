a,b=map(int,input().split())

a-=1
# temp_a=0
#  1로 나눈 값 더함 
temp_a=a

for i in range(1,99):
    temp=(a//(2**i))*((2**i)-(2**(i-1)))
    temp_a+=temp
    

temp_b=b
for i in range(1,99):
    temp=(b//(2**i))*((2**i)-(2**(i-1)))
    temp_b+=temp
print(temp_b-temp_a)