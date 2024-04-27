from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """
    CRUD operations for Animal collection in MongoDB
    """

    def __init__(self, USER, PASS, HOST, PORT, DB, COL):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser2'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32490
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data):
        """
        Insert a document into the specified MongoDB database and collection.
        Return True if successful insert, else False.
        """
        if data is not None:
            result = self.collection.insert_one(data)
            return True if result.inserted_id else False
        else:
            raise Exception("Nothing to save because data parameter is empty")

    def read(self, query):
        """
        Query for documents from the specified MongoDB database and collection.
        Return the result in a list if the command is successful, else an empty list.
        """
        cursor = self.collection.find(query)
        result = [document for document in cursor]
        return result
    
    def update(self, query, newValue):
        """
        Query for and change document(s) from a specified MongoDB database collection
        Return the number of objects modified in the collection.
        """
        result = self.collection.update_many(query, {"$set": newValue})
        return result.modified_count
    
    def delete(self, query):
        """
        Query for and remove document(s) from a specified MongoDB database collection
        Return the number of objects removed from the collection.
        """
        result = self.collection.delete_many(query)
        return result.deleted_count
