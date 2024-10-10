from returns.result import Success

from repository.accident_area_and_cause_repostiory import find_all_accidents_area_cause, find_accidents_by_area_and_cause




def test_find_all_accidents():
   accidents =  find_all_accidents_area_cause()
   print(accidents)
   assert isinstance(accidents,Success)


def test_find_accidents_by_area():

    all_accidents = find_all_accidents_area_cause()
    print(all_accidents.unwrap()[0]["beat_of_occurrence"], all_accidents.unwrap()[0]["primary_cause"])
    accidents =  find_accidents_by_area_and_cause(all_accidents.unwrap()[0]["beat_of_occurrence"], all_accidents.unwrap()[0]["primary_cause"])

    assert all_accidents.value_or([])[0]["beat_of_occurrence"] ==  accidents.value_or({})["beat_of_occurrence"]




