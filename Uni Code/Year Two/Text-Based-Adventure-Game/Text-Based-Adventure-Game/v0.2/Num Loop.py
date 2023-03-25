"Given a range of the first 10 numbers, Iterate from the start number to the end number, and In each iteration print the sum of the current number and previous number"

num = {0,1,2,3,4,5,6,7,8,9,10,11}
cntNum = num
num2 = cntNum
prvNum = num2 - cntNum
add = (cntNum + prvNum)

while(num):
    print("Current Number: ",cntNum, "Previous Number: ",prvNum, "Sum",add)       
        

