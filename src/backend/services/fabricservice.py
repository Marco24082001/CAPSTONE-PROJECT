import requests
import hashlib
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.conf import settings


class FabricService:
    api_url = 'http://192.168.63.128:8000/api/'

    @classmethod
    def getAsset(cls, id):
        if not settings.USE_HYPERLEDGER_FABRIC: return
        res = requests.get(cls.api_url + 'query/' + id)
        asset = json.loads(res.json()['response'])
        return asset

    @classmethod
    def getAllAssets(cls):
        if not settings.USE_HYPERLEDGER_FABRIC: return
        res = requests.get(cls.api_url + 'queryallassets')
        return res.json()
    
    @classmethod
    def addAsset(cls, data, fields):
        if not settings.USE_HYPERLEDGER_FABRIC: return
        # Extract the desired fields from the data
        asset = {field: data[field] for field in fields}
        print('add')
        print(asset)
        # Convert the asset to JSON
        jsonAsset = json.dumps(asset, indent=4, sort_keys=True, cls=DjangoJSONEncoder)
        hash_asset = hashlib.md5(jsonAsset.encode("utf-8")).hexdigest()
        requests.post(cls.api_url + 'addasset', json={'id': asset['id'], 'hash': hash_asset})

    @classmethod
    def updateAsset(cls, data, fields):
        if not settings.USE_HYPERLEDGER_FABRIC: return
        # Extract the desired fields from the data
        asset = {field: data[field] for field in fields}
        # Convert the asset to JSON
        jsonAsset = json.dumps(asset, indent=4, sort_keys=True, cls=DjangoJSONEncoder)
        hash_asset = hashlib.md5(jsonAsset.encode("utf-8")).hexdigest()
        requests.put(cls.api_url + 'changeAsset/' + asset['id'], json = {'hash': hash_asset})
    
    @classmethod
    def deleteAsset(cls, id):
        if not settings.USE_HYPERLEDGER_FABRIC: return
        print('delete')
        requests.delete(cls.api_url + 'deleteAsset/' + id)
        print('thanhvi')
    
    @classmethod
    def isEqualHash(cls, data, fields):
        if not settings.USE_HYPERLEDGER_FABRIC: return True
        # Extract the desired fields from the data
        print('get')
        asset = {field: data[field] for field in fields}
        print(asset)
        # Convert the asset to JSON
        jsonAsset = json.dumps(asset, indent=4, sort_keys=True, cls=DjangoJSONEncoder)
        hash_asset = hashlib.md5(jsonAsset.encode("utf-8")).hexdigest()
        _asset = cls.getAsset(asset['id']) 
        return hash_asset == _asset['hash_value']

# [{"hash_value":"good","id":"07ba10b3-b370-491d-9094-d41fc421c6d0"},{"hash_value":"bad","id":"720eca27-43ba-4e75-90d4-f8e44f8999e4"}]

# {'id': 'cbffff8e-f6de-4ac4-b5ab-2536eaf44e53', 'hash_value': '5d1e6b739c1a4c6cd4c772191d13c23e'}
