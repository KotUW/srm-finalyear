from block import Block
import time

class Blockchain:
    unconfirmedTrns = []
    chain = []

    def CreateGenesisBlock(self):
        genBlk = Block(0, [], time.time(), "0")
        genBlk.hash = genBlk.computeHash()
        self.chain.append(genBlk)
    
    @property
    def lastBlk(self) -> Block:
        return self.chain[-1]

    def pow(self, Block):
    """Proof Of Work used to verify that this server has permision to append."""
    