from hashlib import sha512
import json
# TODO: Replace with msgpack 
# from mood.msgpack import pack, unpack, register

class Block:
    # index:int
    # trn
    # tp:datetime.datetime
    # nounce:int
    # prvHash:str

    def __init__(self, index:int, transactionn, timestamp, prvHash, nounce=0):
        self.id = index
        self.trn = transactionn
        self.tp = timestamp
        self.prvHash = prvHash
        self.nonce = nonce
    
    def computeHash(self):
        blockStr = json.dumps(self.__dict__, sort_keys=True)
        return sha256(blockStr.encode()).hexdigest
