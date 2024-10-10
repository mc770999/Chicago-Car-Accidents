from pymongo import MongoClient


client = MongoClient('mongodb://172.30.156.27:27017')
accidents_info = client['accidents_info']



accident = accidents_info['accident']
accident_by_beat_of_occurrence_and_day = accidents_info['accident_by_beat_of_occurrence_and_day']
accident_by_beat_of_occurrence_and_month = accidents_info['accident_by_beat_of_occurrence_and_month']
accident_by_beat_of_occurrence_and_primary_cause = accidents_info['accident_by_beat_of_occurrence_and_primary_cause']
total_injuries = accidents_info['total_injuries']





