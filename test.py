import csv
with open('HW.csv',newline='')as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

lengthOfList = len(new_data)
sum=0
for y in new_data:
    sum = sum+y

mean = sum/lengthOfList

print("Average is:"+str(mean))