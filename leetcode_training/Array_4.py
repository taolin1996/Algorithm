#Given a non-negative number represneted as an array of digits, plus one to the number
#The digits are stored such that the most significant digit is at the head of list


#意思就是每位都加1，有进位
test = 9999
temp = '1'
for i in range(1,len(str(test))):
    temp += '1'
temp = int(temp)
print(test + temp)
