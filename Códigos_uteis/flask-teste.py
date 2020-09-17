from flask import flask
from flask_restplus import Resource, Api
app = Flask('teste_app')

@app.route('/teste')
@api.doc('params={}')

class TestApp(Resource):
    def get():
        return 'Hello World!'

if __name__ == "__main__":
    app.run(host=HOSTNAME, debug=True)        



import requests
response = requests.get('https://abc.com/def/hello') #simple GET req
json_response = response.json() #response parsed in JSON



import unittest
from unittest.mock import Mock
#importing the module needs to be tested
from flask import app

class AppTest(unittest.TestCase):
  app = app().get()
  self.assertEquals(app, "get")
  self.assertTrue(app=="get")
  #creating mock of requests get call with return value of abc
  app.requests.get = Mock(return_value="abc")
  self.assertEquals(app.get_request(), "abc")
  # asserting if the mocked method is called
  self.assertTrue(app.request.get.called)