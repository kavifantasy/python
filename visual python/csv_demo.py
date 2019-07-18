import csv

path = "C:\\Users\\trainee\\Documents\\python\\movies.csv"
'''
lines = [line for line in open(path)]
print(lines[0])
print(lines[1])

lines[0].strip()
print(lines[0].strip().split(","))

dataset = [line.strip().split(',') for line in open(path)]
print(dataset[0])
print(dataset[1])
'''
file = open(path, newline='')

reader = csv.reader(file)
header = next(reader)
data = [row for row in reader]

print(data[0])


new_data = []
for row in data:
    # print(row)
    title = row[0]
    genre = row[1]
    year = int(row[2])
    new_data.append([title, genre, year])

print(new_data)

return_path = "C:\\Users\\trainee\\Documents\\python\\returns.csv"
file = open(return_path,'w')

writer = csv.writer(file)
writer.writerow(["Title","Date"])

for i in range(len(data)):
    row = data[i]
    title = row[0]
    year = row[2]
    writer.writerow([title,year])

file.close()