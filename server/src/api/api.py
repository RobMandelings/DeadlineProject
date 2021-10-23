"""
File contains the api instance and initializes all resources with a corresponding route
"""

import flask_restful

api = flask_restful.Api()

# api.add_resource(task_resources.TaskResource, '/api/tasks/<string:task_id>')