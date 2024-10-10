from bson import ObjectId
from returns.result import Success, Failure

from database.connect import accident_area_cause

def find_accidents_by_area_and_cause(area, cause,):
    try:
        one_accidents = accident_area_cause.find_one({
            "beat_of_occurrence": float(area),
            "primary_cause": cause
        })
        return Success(one_accidents)
    except Exception as e:
        return Failure(e)

def find_all_accidents_area_cause():
    all_accidents = accident_area_cause.find({}).to_list()

    if all_accidents:
        return Success(all_accidents)
    else:
        return Failure("find operation failed.")
