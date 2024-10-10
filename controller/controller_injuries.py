from flask import Flask, jsonify, request, Blueprint
import repository.injuries_repository as repo_injuries
import repository.accidents_area_repository as repo_accidents_area
import repository.accidents_day_area_repository as repo_area_day
import repository.accident_area_month_repository as repo_area_month
import repository.accident_area_and_cause_repostiory as repo_area_cause
import repository.accidents_week_area_repository as repo_area_week
from returns.result import Success, Failure
import json
from bson import json_util

def parse_json(data):
    return json.loads(json_util.dumps(data))

# Convert Success and Failure to JSON
def response_format(result):
    if isinstance(result, Success):
        return jsonify({"success": True, "message": parse_json(result.unwrap())}), 200  # Use unwrap() to get the value from Success
    elif isinstance(result, Failure):
        return jsonify({"success": False, "message": str(result.failure())}), 400  # Use failure() to get the error message

blueprint = Blueprint('blueprint', __name__)

# Find injuries by id
@blueprint.route('/injuries/<string:id>', methods=['GET'])
def find_injuries_by_id(id):
    injuries = repo_injuries.find_injuries_by_id(id)
    return response_format(injuries)  # No need for extra checks, response_format will handle Success or Failure

# Find all injuries
@blueprint.route('/injuries/', methods=['GET'])
def find_all_injuries():
    injuries = repo_injuries.find_all_injuries()
    print(injuries.unwrap())
    return response_format(injuries)  # Same here, response_format will handle it

# Find accidents by area
@blueprint.route('/accidents_area/<string:area>', methods=['GET'])
def find_accidents_by_id(area):
    accidents = repo_accidents_area.find_accidents_by_area(area)
    return response_format(accidents)  # No need for extra checks, response_format will handle Success or Failure

# Find all accidents
@blueprint.route('/accidents_area/', methods=['GET'])
def find_all_accidents():
    accidents = repo_accidents_area.find_all_accidents()
    print(accidents.unwrap())
    return response_format(accidents)  # Same here, response_format will handle it


# Find all accidents
@blueprint.route('/area_and_day/<string:area>/<string:day>', methods=['GET'])
def find_accident_area_and_day(area,day):
    accidents = repo_area_day.find_accidents_by_area_and_day(area,day)
    print(accidents.unwrap())
    return response_format(accidents)  # Same here, response_format will handle it



@blueprint.route('/area_and_cause/<string:area>/<string:cause>', methods=['GET'])
def find_accident_area_and_month(area,cause):
    accidents = repo_area_cause.find_accidents_by_area_and_cause(area,cause)
    print(accidents.unwrap())
    return response_format(accidents)  # Same here, response_format will handle it





@blueprint.route('/area_and_month/<string:area>/<string:month>', methods=['GET'])
def find_accident_area_and_cause(area,month):
    accidents = repo_area_month.find_accidents_by_area_and_month(area,month)
    print(accidents.unwrap())
    return response_format(accidents)  # Same here, response_format will handle it


@blueprint.route('/area_and_week/<string:area>/<string:month>', methods=['GET'])
def find_accident_area_week(area,month):
    accidents = repo_area_week.find_accidents_by_area_and_week(area,month)
    print(accidents.unwrap())
    return response_format(accidents)  # Same here, response_format will handle it




