from run import app
from flask_testing import TestCase
import json
#import requests

class Tests(TestCase):

    def create_app(self):
        return app

#create a request

    def test_create_request(self):
        with self.client:
            post_data = ({'name':'lakeli', 'username':'seada'})
            response = self.client.post('/users/requests', content_type = 'application/json', data =json.dumps(post_data))
            reply = json.loads(response.data.decode())
            self.assertEquals(reply['status_code'], 'lakeli')

#fetch request id for a logged in user
    def test_fetch_id(self):
        with self.client:
            post_data = ({'name':'lakeli', 'username':'seada'})
            response = self.client.get('/users/requests/requestID', content_type = 'application/json', data =json.dumps(post_data))
            reply = json.loads(response.data.decode())
            self.assertEquals(reply['name'],'lakeli' )
#modify a request
    def test_modify_request(self):
        with self.client:
            post_data = ({'name':'lakeli', 'username':'seada'})
            response = self.client.get('/users/requests/requestID', content_type = 'application/json', data =json.dumps(post_data))
            reply = json.loads(response.data.decode())
            self.assertEquals(reply['name'],'lakeli' )
#fetch all requests
    def test_fetch_all_requests(self):
        with self.client:
            post_data = ({'name':'lakeli', 'username':'seada'})
            response = self.client.get('/users/requests/requestID', content_type = 'application/json', data =json.dumps(post_data))
            reply = json.loads(response.data.decode())
            self.assertEquals(reply['name'],'lakeli' )

