# BLOCKCHAIN PROCESS
import datetime
import hashlib

class Block:
    blockNo:int = 0
    data:str = None
    nextp = None
    hashb:str = None
    nonce:int = 0
    previous_hash:str = 0x0
    timestamp:datetime.datetime = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"

class Blockchain:
    "The Blockchain"
    diff = 20
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis")
    dummy = head = block

    def add(self, block):

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.nextp = block
        self.block = self.block.nextp
    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

if __name__ == "__main__":
    blockchain = Blockchain()

    for n in range(5):
        start = datetime.datetime.now()
        blockchain.mine(Block("Block " + str(n+1)))
        print(f"Took {(datetime.datetime.now() - start).total_seconds()} secounds to complete.")

    # while blockchain.head.nextp != None:
    #     print(blockchain.head)
    #     blockchain.head = blockchain.head.nextp