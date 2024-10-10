from returns.result import Success

from repository.accidents_day_area_repository import find_all_accidents_area_day, find_accidents_by_area_and_day




def test_find_all_accidents():
   accidents =  find_all_accidents_area_day()
   print(accidents)
   assert isinstance(accidents,Success)


def test_find_accidents_by_area():

    all_accidents = find_all_accidents_area_day()
    print(all_accidents.unwrap()[0]["beat_of_occurrence"], all_accidents.unwrap()[0]["day"])
    accidents =  find_accidents_by_area_and_day(all_accidents.unwrap()[0]["beat_of_occurrence"], all_accidents.unwrap()[0]["day"])

    assert all_accidents.value_or([])[0]["beat_of_occurrence"] ==  accidents.value_or({})["beat_of_occurrence"]




