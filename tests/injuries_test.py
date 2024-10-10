
import pytest
from jinja2.lexer import Failure
from pymongo.collection import Collection
from returns.result import Success

from repository.injuries_repository import find_all_injuries, find_injuries_by_id




def test_find_all_injuries():
   injuries =  find_all_injuries()
   print(injuries)
   assert isinstance(injuries,Success)


def test_find_injuries_by_id():
   injuries = find_all_injuries()
   injuries =  find_injuries_by_id(injuries.value_or([])["_id"])
   assert injuries.value_or([])[0]["brand"] ==  injuries.value_or({})["brand"]





