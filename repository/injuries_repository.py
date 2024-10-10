from bson import ObjectId
from returns.result import Success, Failure

from database.connect import injuries

def find_injuries_by_area(area):
    one_injuries = injuries.find_one({"beat_of_occurrence" : int(area)})
    if one_injuries:
        return Success(one_injuries)
    else:
        return Failure("find operation failed.")

def find_all_injuries():
    all_injuries = injuries.find({}).to_list()

    if all_injuries:
        return Success(all_injuries)
    else:
        return Failure("find operation failed.")
