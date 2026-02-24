# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Additional requirments to constructor added for M6 Milestone
        
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username #'aacuser'
        PASS = password #'1212'
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            self.database.animals.insert_one(data)
            confirmation = bool(self.read(data))
            return confirmation
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    def read(self, data):
        cursor = self.database.animals.find(data)
        return cursor
    
    def update_onee(self, find, update):
        if find is not None:
            updated = self.database.animals.update_one(find, update)
            return updated.modified_count
        else:
            raise Exception("Nothing to update, because find parameter is empty")
            
    def update_many(self, find, update):
        if find is not None:
            updated = self.database.animals.update_many(find, update)
            return updated.modified_count
        else:
            raise Exception("Nothing to update, because find parameter is empty")
            
    def delete_one(self, data):
        if data is not None:
            beforeCount = self.database.animals.count_documents({})
            self.database.animals.delete_one(data)
            afterCount = self.database.animals.count_documents({})
            deleteCount = beforeCount - afterCount
            return deleteCount
        else:
            raise Exception("Nothing to delete, because data parameter is empty")
            
    def delete_many(self, data):
        if data is not None:
            beforeCount = self.database.animals.count_documents({})
            self.database.animals.delete_many(data)
            afterCount = self.database.animals.count_documents({})
            deleteCount = beforeCount - afterCount
            return deleteCount
        else:
            raise Exception("Nothing to delete, because data parameter is empty")
            