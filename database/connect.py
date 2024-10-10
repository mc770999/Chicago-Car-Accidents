from pymongo import MongoClient


client = MongoClient('mongodb://172.30.156.27:27017')
accidents_info = client['accidents_info']



accidents = accidents_info['db_accident']
accident_area_day = accidents_info['db_accident_area_day']
accident_area_week = accidents_info['db_accident_area_week']
accident_area_month = accidents_info['db_accident_area_month']
accident_area_cause = accidents_info['db_accident_area_cause']
injuries = accidents_info['db_injuries']





