#  CRUD Operations Using PyMongo in Python

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["testdatabase"]
collection = db["test-collection"]

# Document to insert
doc = {"Athar": 1, "Sayed": 2, "Abbas": 3}

# Insert the document
insert_result = collection.insert_one(doc)
print("Inserted ID:", insert_result.inserted_id)

# Find the document before deleting
found_doc = collection.find_one(doc)
if found_doc:
    deleted_id = found_doc["_id"]
    # Now delete the document using the _id
    delete_result = collection.delete_one({"_id": deleted_id})
    if delete_result.deleted_count == 1:
        print("Deleted document ID was:", deleted_id)
    else:
        print("Document was not deleted.")
else:
    print("Document not found.")
