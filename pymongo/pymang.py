import pymongo
#create connection to MongoDB
client=pymongo.MongoClient('mongodb://localhost:27017')
mydb=client['persons']

#list system databases
print(client.list_database_names())

#Check if 'persons' database exists
dbList=client.list_database_names()
if 'persons' in  dbList:
    print("'Persons' db exists")
else:
    print("'persons' db doesnot exists!")
    
#use 'persons' database    
mydb=client['persons']

#Create collection called customers
mycol=mydb['customers']

#list all the collections in database
colList=mydb.list_collection_names()
print(colList)

#Check if the 'customers' collection is exists
colList=mydb.list_collection_names()
if 'customers' in colList:
    print("'customers' Collection exists")
else:
    print("'customers' collection doesn't exists")

#insert document
dict={'rollNo':19,'name':'John','age':12}
obj=mycol.insert_one(dict)  #returns Object
print(obj)
print(obj.inserted_id)   #returns id of inserted document


#insert multiple documents
stdList=[{'rollNo':13,'name':'Sandy','age':10},{'rollNo':14,'name':'Vicky','age':10},{'rollNo':15,'name':'Ben','age':10}]

x=mycol.insert_many(stdList)
print(x.inserted_ids)  #returns inserted documents _ids

#insert multiple documents with specified ID's, id's must be unique

stdList1=[
    {"_id":21,'rollNo':13,'name':'Sandy','age':10},{"_id":22,'rollNo':14,'name':'Vicky','age':10},{"_id":23,'rollNo':15,'name':'Ben','age':10},
]
x=mycol.insert_many(stdList1)
print(x.inserted_ids)

##find_one() method returns the first occurence in the selection
print(my_col.find_One())

##find_one() method returns all the first occurence in the selection
for c in mycol.find():
    print (c)

##Return selected fields, We can't specify 0 and 1 values in :
##except _id field
for x in mycol.find({},{'_id':0,'name':1,'age':1}):
    print(x)
##Query
doc=mycol.find({'name':'Rahul'})
for d in doc:
    print(d)
#Query based on modifier
gt,gte,le,lte,
docs=mycol.find({'name':{'$gt':'T'}})
for d in docs:
    print(d)
#filter with regular expressions
docs=mycol.find({'name':{'$regex':'y$'}})
for d in docs:
    print(d)


docs=mycol.find().sort('name')
for d in Docs:
    print(d)
##sort(),descending order
docs=mycol.find().sort('name',-1)
for d in Docs:
    print(d)
##delete_One(), deletes specified document
mycol.delete_one({'name':'Rahul'})

