import csv
from time import strptime

import pandas as pd
from bson import ObjectId
from pymongo import MongoClient
from database.connect import *
from datetime import timedelta, datetime



# MongoDB connection setup
def init_mongo(db_name, collection_name):
    client = MongoClient('mongodb://localhost:27017/')
    db = client[db_name]
    collection = db[collection_name]
    return collection

def if_none_o(value):
    return value if value is not None else 0


def get_week_range(date_str):

    # Convert the string to a datetime object
    date_format = "%m-%d-%Y"
    date_obj = datetime.strptime(date_str, date_format)

    # Add the specified number of days
    new_date = date_obj + timedelta(days=6)

    # Format the new date as a string in the same format
    new_date_str = new_date.strftime("%d-%m-%Y")

    return new_date_str

def insert_all_collections(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        import_csv_to_mongo_accidents(row,accidents)
        upsert_accidents_from_csv_accident_day(row, accident_area_day)
        import_csv_to_mongo_accident_month(row, accident_area_month)
        import_primary_cause_to_mongo(row, accident_area_cause)
        import_total_injuries_to_mongo(row, injuries)
        upsert_accidents_from_csv_accident_week(row, accident_area_week)


def import_csv_to_mongo_accidents(row, collection):

    document = {
        "crash_record_id": row["CRASH_RECORD_ID"],
        "crash_date": pd.to_datetime(row["CRASH_DATE"]),
        "beat_of_occurrence": row["BEAT_OF_OCCURRENCE"],
        "total_injuries": if_none_o(row["INJURIES_TOTAL"]),
        "fatal_injuries": if_none_o(row["INJURIES_FATAL"]),
        "non_fatal_injuries": if_none_o(row["INJURIES_NON_INCAPACITATING"]),
        "street_name": row["STREET_NAME"],
        # Add other necessary fields here
    }

    # Check if the document already exists
    existing_document = collection.find_one({"crash_record_id": document["crash_record_id"]})

    if existing_document:
        # Update the existing document
        pass
    else:
        # Insert the new document
        collection.insert_one(document)




def upsert_accidents_from_csv_accident_day(row, collection):

    day = pd.to_datetime(row['CRASH_DATE']).strftime('%m-%d-%Y')  # Format as needed
    beat_of_occurrence = row['BEAT_OF_OCCURRENCE']

    # Calculate the sum of accidents (for this example, just a count, you can modify it as needed)
    sum_accidents = 1  # Assuming each row represents one accidents

    # Create a document for the current row
    accident_record = {
        "day": day,
        "beat_of_occurrence": beat_of_occurrence,
        "sum_accidents": sum_accidents
    }

    # Check if the document already exists by beat_of_occurrence and month
    existing_record = collection.find_one({
        "beat_of_occurrence": accident_record["beat_of_occurrence"],
        "day": accident_record["day"]
    })

    if existing_record:
        # Update the existing document
        collection.update_one({"day": accident_record["day"]}, {"$inc": {"sum_accidents": 1}})
    else:
        # Insert the new document
        collection.insert_one(accident_record)

def upsert_accidents_from_csv_accident_week(row, collection):

    day = pd.to_datetime(row['CRASH_DATE']).strftime('%m-%d-%Y')  # Format as needed
    beat_of_occurrence = row['BEAT_OF_OCCURRENCE']

    # Calculate the sum of accidents (for this example, just a count, you can modify it as needed)
    sum_accidents = 1  # Assuming each row represents one accidents
    print(day)
    # Create a document for the current row
    accident_record = {
        "start_day": day,
        "end_day" :  get_week_range(day),
        "beat_of_occurrence": beat_of_occurrence,
        "sum_accidents": sum_accidents
    }

    # Check if the document already exists by beat_of_occurrence and month
    existing_record = collection.find_one({
        "beat_of_occurrence": accident_record["beat_of_occurrence"],
        "start_day": {"$gte" : day},
        "end_day" : {"$lte" : day}
    })

    if existing_record:
        # Update the existing document
        collection.update_one({"_id": existing_record["_id"]}, {"$inc": {"sum_accidents": 1}})
    else:
        # Insert the new document
        collection.insert_one(accident_record)



# Function to import accidents statistics by beat of occurrence and month from CSV
def import_csv_to_mongo_accident_month(row, collection):
    # Extract necessary fields
    beat_of_occurrence = row['BEAT_OF_OCCURRENCE']
    month = pd.to_datetime(row['CRASH_DATE']).strftime('%m')  # Get month from CRASH_DATE

    accident_record = {
        "beat_of_occurrence": beat_of_occurrence,
        "month": month,
        "sum_accidents": 1  # Start with 1 for this record
    }

    # Check if the document already exists by beat_of_occurrence and month
    existing_record = collection.find_one({
        "beat_of_occurrence": accident_record["beat_of_occurrence"],
        "month": accident_record["month"]
    })

    if existing_record:
        # Update the existing document to increment the sum of accidents
        collection.update_one({"month": existing_record["month"]}, {"$inc": {"sum_accidents": 1}})
    else:
        # Insert the new document
        collection.insert_one(accident_record)



def import_primary_cause_to_mongo(row, collection):
    sum_accidents = 1

    accident_record = {
        "primary_cause": row["PRIM_CONTRIBUTORY_CAUSE"], # Primary cause of the accidents
        "beat_of_occurrence": row["BEAT_OF_OCCURRENCE"],  # Beat of occurrence
        "sum_accidents": sum_accidents,                # Assuming NUM_UNITS is the number of accidents
        # Add other necessary fields here if required
    }

    existing_record = collection.find_one({
        "beat_of_occurrence": accident_record["beat_of_occurrence"],
        "primary_cause": accident_record["primary_cause"]
    })

    if existing_record:
        # Update the existing document
        collection.update_one({"_id": ObjectId(existing_record["_id"])}, {"$inc": {"sum_accidents": 1}})
    else:
        # Insert the new document
        collection.insert_one(accident_record)

def import_total_injuries_to_mongo(row, collection):

    sum_accidents = 1

    accident_record = {
        "total_injuries": if_none_o(row["INJURIES_TOTAL"]),
        "fatal_injuries": if_none_o(row["INJURIES_FATAL"]),
        "non_fatal_injuries": if_none_o(row["INJURIES_NON_INCAPACITATING"]),
        "beat_of_occurrence": row["BEAT_OF_OCCURRENCE"],
        "sum_accidents": sum_accidents,
        "list_of_accident_info": [row["CRASH_RECORD_ID"]]
    }

    # Check if the document already exists
    existing_record = collection.find_one({
        "beat_of_occurrence": accident_record["beat_of_occurrence"]
    })

    if existing_record:
        # Update the existing document
        collection.update_one(
            {"_id": ObjectId(existing_record["_id"])},
            {
                "$push": {
                    "list_of_accident_info": row["CRASH_RECORD_ID"]  # Push the crash ID to the list
                },
                "$inc": {
                    "sum_accidents": 1,
                    "total_injuries" : if_none_o(row["INJURIES_TOTAL"]),
                    "fatal_injuries": if_none_o(row["INJURIES_FATAL"]),
                    "non_fatal_injuries": if_none_o(row["INJURIES_NON_INCAPACITATING"])
                }
            }
        )
    else:
        # Insert the new document
        collection.insert_one(accident_record)

def create_indexes():
    


insert_all_collections("../data/data.csv")

