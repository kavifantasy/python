import csv
path="C:\\Users\\admin\\Desktop\\visual python\\movie.csv"
lines=[line for line in open(path)]
print(lines[0])
print(lines[1])

#split lines into list
print(lines[0].strip().split(','))


#this code is to do the same as above while reading itself
dataset=[line.strip().split(',') for line in open(path)]
print(dataset)

#prints the same except header using reader function
file=open(path,newline='')
#newline value is given as in diff platforms diff values will be used
#so we assign to null value
#csv module has reader function to read file
reader=csv.reader(file)
#reader has the location of file
header=next(reader) #point to first line
data=[row for row in reader]#read from second line
print(data)
print(header)

new_data=[]
for row in data:
    print(row)
    title=row[0]
    genre=row[1]
    year=int(row[2])
    new_data.append([title,genre,year])
print(new_data)


return_path="C:\\Users\\admin\\Desktop\\visual python\\returns.csv"
file=open(return_path,'w')
writer = csv.writer(file)
#manually writing to csv file
writer.writerow(['Title','Date'])
#copying to csv file
for i in range(len(data)):
    row=data[i]
    title=row[0]
    year=row[2]
    writer.writerow([title,year])
file.close()

