from hashlib import sha512
import time
import json

class Block:
    index:int    # The Block number
    msg:str      # An Array of messages user sent
    tp:time      # The time of driving the proof (use for conflict resolution)
    nounce:int   # The nounce. (required for the proof of work Implementation.)
    prvHash:str  # The hash of the previous hash in the Block Chain

    def __init__(self, index:int, message, timestamp, prvHash, nounce=0):
        self.id = index
        self.msg = message
        self.tp = timestamp
        self.prvHash = prvHash
        self.nonce = nonce
    
    def computeHash(self):
        """Computing hash form a message"""

        # Using Json beacuse str one is unrelaible and produces exactly the same output
        blockStr = json.dumps(self.__dict__, sort_keys=True)
        return sha256(blockStr.encode()).hexdigest


class Blockchain:
    chain = []
    difficulty = 1

    def CreateGenesisBlock(self, diff) -> None:
        genBlk = Block(0, [], time.time(), "0")
        genBlk.hash = genBlk.computeHash()
        
        self.chain.append(genBlk)
        self.difficulty = diff
    
    @property
    def lastBlck(self) -> Block:
        return self.chain[-1]

    def pow(self, blck):
        """Proof Of Work used to verify that this server has permision to append."""
        blck.nounce = 0
        computedHash:str = blck.computeHash()

        while not computedHash.startswith('0' * self.difficulty):
            blck.nonce += 1
            computedHash = blck.computeHash()
    
        return computedHash

    def isValidProof(self, Blck, blckHash) -> bool:
        """Check a Block's Proof before appending it to the chain"""
        return (blckHash.startswith('0' * self.difficulty) and blckHash == blck.completeHash())

    def addBlck(self, blck, proof) -> bool:
        """Fucnction to add Unconfirmed Blocks."""
        prevBlck = self.lastBlck.hash
        if prevBlck != blck.prevBlck:
            throw("Not Synced with Chain different last blocks")
            return False

        if not self.isValidProof(blck, proof):
            return False
        
        blck.hash = proof
        self.chain.append(blck)
        return True


