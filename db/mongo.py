from pymongo import MongoClient
from dotenv import load_dotenv
import os
import sys

# Load environment variables
load_dotenv()

class DatabaseConnection:
    _instance = None
    _client = None
    _db = None

    def __init__(self):
        # Ensure connection is established immediately
        if not DatabaseConnection._client:
            self.connect()

    def connect(self):
        try:
            # Retrieve MongoDB connection string from environment variable
            mongo_uri = os.getenv('MONGO_URI')
            
            if not mongo_uri:
                raise ValueError("MongoDB URI not found in environment variables")
            
            # Create MongoDB client
            DatabaseConnection._client = MongoClient(mongo_uri)
            
            # Verify connection
            DatabaseConnection._client.admin.command('ismaster')
            print("Successfully connected to MongoDB")
            
            # Set database (replace with your actual database name)
            DatabaseConnection._db = DatabaseConnection._client['college_project']
        
        except Exception as e:
            print(f"Critical Error connecting to MongoDB: {e}")
            print("Exiting application due to database connection failure")
            sys.exit(1)  # Exit the application if database connection fails

    @classmethod
    def get_database(cls):
        """
        Get the database instance
        """
        if not cls._db:
            cls._instance = DatabaseConnection()
        return cls._db

    @classmethod
    def get_collection(cls, collection_name):
        """
        Get a specific collection from the database
        """
        db = cls.get_database()
        return db[collection_name]

# Create the connection immediately when the module is imported
db_connection = DatabaseConnection()