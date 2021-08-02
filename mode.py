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

data = Counter(new_data)

moderange = {
    "50-60":0,
    "60-70":0,
    "70-80":0
}

for height, occurence in data.items():
    if 50< float(height) <60:
        moderange["50-60"]=moderange["50-60"]+occurence
    elif 60< float(height) <70:
        moderange["60-70"]=moderange["60-70"]+occurence
    elif 70< float(height) <80:
        moderange["70-80"]=moderange["70-80"]+occurence

