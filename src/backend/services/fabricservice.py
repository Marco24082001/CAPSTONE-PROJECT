import requests
import hashlib
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.conf import settings


class FabricService:
    api_url = 'http://192.168.63.128:8080/api/'
    @classmethod
    def getAsset(cls, id):
        if settings.USE_HYPERLEDGER_FABRIC:
            res = requests.get(cls.api_url + 'query/' + id)
            asset = json.loads(res.json()['response'])
            return asset

    @classmethod
    def getAllAssets(cls):
        if settings.USE_HYPERLEDGER_FABRIC:
            res = requests.get(cls.api_url + 'queryallassets')
            return res.json()
    
    @classmethod
    def addAsset(cls, asset):
        if settings.USE_HYPERLEDGER_FABRIC:
            jsonAsset = json.dumps(asset,indent=4, sort_keys=True, cls=DjangoJSONEncoder)
            hash_asset = hashlib.md5(jsonAsset.encode("utf-8")).hexdigest()
            print(hash_asset)
            res = requests.post(cls.api_url + 'addasset', json={'id': asset['id'], 'hash': hash_asset})
            print({
                'id': asset['id'],
                'hash_value': hash_asset
            })
            print(res.status_code)
            # return res.status_code
    
    @classmethod
    def updateAsset(cls, asset):
        if settings.USE_HYPERLEDGER_FABRIC:
            jsonAsset = json.dumps(asset,indent=4, sort_keys=True, cls=DjangoJSONEncoder)
            hash_asset = hashlib.md5(jsonAsset.encode("utf-8")).hexdigest()
            res = requests.put(cls.api_url + 'changeAsset/' + asset['id'], json = {'hash': hash_asset})
            return res.status_code
    
    @classmethod
    def isEqualHash(cls, asset):
        if settings.USE_HYPERLEDGER_FABRIC:
            jsonAsset = json.dumps(asset,indent=4, sort_keys=True, cls=DjangoJSONEncoder)
            hash_asset = hashlib.md5(jsonAsset.encode("utf-8")).hexdigest()
            _asset = cls.getAsset(asset['id'])
            # print(asset['id'])
            # print(hash_asset)
            # print(_asset['hash_value'])
            return hash_asset == _asset['hash_value']

# FabricService.getAsset('07ba10b3-b370-491d-9094-d41fc421c6d0')
# # FabricService.getAllAssets()
# FabricService.updateAsset('vothanhvi')

# [{"hash_value":"good","id":"07ba10b3-b370-491d-9094-d41fc421c6d0"},{"hash_value":"bad","id":"720eca27-43ba-4e75-90d4-f8e44f8999e4"}]

# {'id': 'cbffff8e-f6de-4ac4-b5ab-2536eaf44e53', 'hash_value': '5d1e6b739c1a4c6cd4c772191d13c23e'}