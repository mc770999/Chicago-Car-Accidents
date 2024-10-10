from bson import ObjectId
from returns.result import Success, Failure

from database.connect import accident_area_day

def find_accidents_by_area_and_day(area, day,):
    try:
        one_accidents = accident_area_day.find_one({
            "beat_of_occurrence": float(area),
            "day": day
        })
        return Success(one_accidents)
    except Exception as e:
        return Failure(e)

def find_all_accidents_area_day():
    all_accidents = accident_area_day.find({}).to_list()

    if all_accidents:
        return Success(all_accidents)
    else:
        return Failure("find operation failed.")
