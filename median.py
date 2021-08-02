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
new_data.sort()

if lengthOfList % 2==0:
    median1 = float(new_data[lengthOfList//2])

    median2 = float(new_data[lengthOfList//2-1])

    sumofmedian = median1+median2

    finalMedian = sumofmedian/2
else:
    finalMedian = new_data[lengthOfList//2]

print("Median is:"+str(finalMedian))