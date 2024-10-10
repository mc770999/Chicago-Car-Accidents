
import pytest
from jinja2.lexer import Failure
from pymongo.collection import Collection
from returns.result import Success

from repository.accidents_area_repository import find_all_accidents, find_accidents_by_area




def test_find_all_accidents():
   accidents =  find_all_accidents()
   print(accidents)
   assert isinstance(accidents,Success)


def test_find_accidents_by_area():
   accidents = find_all_accidents()
   accidents =  find_accidents_by_area(accidents.unwrap()[0]["beat_of_occurrence"])
   assert accidents.value_or([])["beat_of_occurrence"] ==  accidents.value_or({})["beat_of_occurrence"]




