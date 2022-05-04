from blockchain import Blockchain, Block
import time

class MessageQueue:
    unconfirmedMsgs = []
    chain:Blockchain

    def __init__(self):
        self.chain = Blockchain(1)
        self.chain.CreateGenesisBlock()

    def mine(self) -> int:
        """Basic Mining Function that go through any unconfirmed transactions and try to append them to the blockchain"""
        if not self.unconfirmedMsgs:
            return False
        
        lstBlck = self.chain.lastBlck

        newBlck = Block(message = self.unconfirmedMsgs,
                        timestamp = time.time(),
                        prvHash = lstBlck.hash,
                        index=lstBlck.id + 1,)
        
        proof = self.chain.pow(newBlck)
        self.chain.addBlck(newBlck, proof)
        self.unconfirmedMsgs = []

        return newBlck.id

    def addNewMsg(self, msg) -> None:
        self.unconfirmedMsgs.append(msg)

    def getQueue(self) -> int:
        return len(self.unconfirmedMsgs)
