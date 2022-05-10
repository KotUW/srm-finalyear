from hashlib import sha512
import time
# import json

class Block:
    id:int         # The Block number
    msg:str # An Array of messages user sent
    tp:time        # The time of driving the proof (use for conflict resolution)
    nounce:int     # The nounce. (required for the proof of work Implementation.)
    prvHash:str    # The hash of the previous hash in the Block Chain

    def __init__(self, index, message, timestamp, prvHash, nounce=0):
        self.id = index
        self.msg = message
        self.tp = timestamp
        self.prvHash = prvHash
        self.nounce = nounce
    
    def computeHash(self):
        """Computing hash form a message"""

        h = sha512()
        h.update(
        str(self.id).encode('utf-8') +
        str(self.msg).encode('utf-8') +
        str(self.prvHash).encode('utf-8') +
        str(self.tp).encode('utf-8') +
        str(self.nounce).encode('utf-8')
        )

        return h.hexdigest()
        # Using Json beacuse str one is unrelaible and produces exactly the same output
        # blockStr = json.dumps(self.__dict__, sort_keys=True)
        # return sha512(blockStr.encode()).hexdigest
    
    def __str__(self):
        return "Block Hash: " + str(self.computedHash()) + "\nBlockNo: " + str(self.id) + "\nBlock Data: " + str(self.msg) + "\nHashes: " + str(self.nonce) + "\n--------------"
    

class Blockchain:
    chain:list
    difficulty:int

    def __init__(self, diff):
        self.chain = []
        self.difficulty = diff

    def CreateGenesisBlock(self) -> None:
        """The First Block of the block chain"""
        genBlk = Block(0, [], time.time(), 0)
        genBlk.hash = genBlk.computeHash()
        
        self.chain.append(genBlk)
    
    @property
    def lastBlck(self) -> Block:
        return self.chain[-1]

    def pow(self, blck):
        """Proof Of Work used to verify that this server has permision to append."""
        blck.nounce = 0
        computedHash:str = blck.computeHash()

        while not computedHash.startswith('0' * self.difficulty):
            blck.nounce += 1
            computedHash = blck.computeHash()
    
        return computedHash

    def isValidProof(self, blck, blckHash) -> bool:
        """Check a Block's Proof before appending it to the chain"""
        return (blckHash.startswith('0' * self.difficulty) and blckHash == blck.computeHash())

    def addBlck(self, blck, proof) -> bool:
        """Fucnction to add Unconfirmed Blocks."""
        prvBlck = self.lastBlck.hash
        if prvBlck != blck.prvHash:
            # raise Exception("Not Synced with Chain different last blocks")
            return False

        if not self.isValidProof(blck, proof):
            return False
        
        blck.hash = proof
        self.chain.append(blck)
        return True

    # Could be optimized by caching the result
    def getBlock(self,BlockId:str) -> Block:
        return self.chain[BlockId]

    def printChain() -> None:
        """Prints th whole chain"""
        for blck in self.chain:
            print(blck)
            print("\nBlock was mined at ", blck.tp, " =========" )
