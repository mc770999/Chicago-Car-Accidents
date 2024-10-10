from returns.result import Success

from repository.accident_area_month_repository import find_all_accidents_area_month, find_accidents_by_area_and_month




def test_find_all_accidents():
   accidents =  find_all_accidents_area_month()
   print(accidents)
   assert isinstance(accidents,Success)


def test_find_accidents_by_area():

    all_accidents = find_all_accidents_area_month()
    print(all_accidents.unwrap()[0]["beat_of_occurrence"], all_accidents.unwrap()[0]["month"])
    accidents =  find_accidents_by_area_and_month(all_accidents.unwrap()[0]["beat_of_occurrence"], all_accidents.unwrap()[0]["month"])

    assert all_accidents.value_or([])[0]["beat_of_occurrence"] ==  accidents.value_or({})["beat_of_occurrence"]




