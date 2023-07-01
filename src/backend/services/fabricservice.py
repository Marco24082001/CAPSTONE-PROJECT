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
        if res.status_code == 500:
            asset = None
        else:
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
        requests.delete(cls.api_url + 'deleteAsset/' + id)
    
    @classmethod
    def isEqualHash(cls, data, fields):
        if not settings.USE_HYPERLEDGER_FABRIC: return True
        # Extract the desired fields from the data
        asset = {field: data[field] for field in fields}
        # Convert the asset to JSON
        jsonAsset = json.dumps(asset, indent=4, sort_keys=True, cls=DjangoJSONEncoder)
        hash_asset = hashlib.md5(jsonAsset.encode("utf-8")).hexdigest()
        _asset = cls.getAsset(asset['id'])
        # sync data from db to blockchain
        # if not _asset:
        #     cls.addAsset(data, fields)
        #     return True
        return hash_asset == _asset['hash_value']
