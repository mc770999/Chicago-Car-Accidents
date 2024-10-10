from bson import ObjectId
from returns.result import Success, Failure

from database.connect import accidents

def find_accidents_by_area(area):
    one_accidents = accidents.find_one({"beat_of_occurrence" : float(area)})
    if one_accidents:
        return Success(one_accidents)
    else:
        return Failure("find operation failed.")

def find_all_accidents():
    all_accidents = accidents.find({}).to_list()

    if all_accidents:
        return Success(all_accidents)
    else:
        return Failure("find operation failed.")
