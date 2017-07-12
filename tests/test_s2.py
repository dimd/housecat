import json
import unittest

import pymongo

import s2.factory


class S2TestCase(unittest.TestCase):
    def setUp(self):
        config = {
            'TESTING': True,
            'MONGO_DBNAME': 'test'
        }
        app = s2.factory.create_app(config)
        self.client = app.test_client()
        self.mongo = pymongo.MongoClient('db')
        db = self.mongo.test
        with open('tests/fixtures/properties.json', 'r') as f:
            db.properties.insert_many(json.load(f))

    def tearDown(self):
        self.mongo.test.properties.remove({})
        self.mongo.close()

    def test_list_all_properties(self):
        rv = self.client.get('/api/properties')
        with open('tests/fixtures/properties.json', 'r') as f:
            assert json.load(f) == json.loads(rv.data)

    def test_list_with_parameters(self):
        rv = self.client.get('/api/properties?'
                             'Availability=Sale&'
                             'Location=Athens&'
                             'Location=Patra&'
                             'minPrice=1000000&'
                             'maxPrice=1000000&'
                             'minSquareMeters=900&'
                             'maxSquareMeters=1100&'
                             'Type=Apartment&'
                             'Type=Maisonette')

        assert json.loads(rv.data) == [{
            'Location': 'Athens',
            'Availability': 'Sale',
            'ID': 1,
            'Price': 1000000,
            'Square Meters': 1000,
            'Type': [
                'Apartment'
            ]
        }]
