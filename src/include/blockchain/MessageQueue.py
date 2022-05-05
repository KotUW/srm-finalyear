from blockchain import Blockchain, Block
import time

class MessageQueue:
    unconfirmedMsgs:list = []
    blockchain:Blockchain
    currBlock = 0

    def __init__(self):
        self.blockchain = Blockchain(1)
        self.blockchain.CreateGenesisBlock()

    def PushMsgs(self) -> None:
        """Basic Mining Function that go through any unconfirmed transactions and try to append them to the blockblockchain"""
        if not self.unconfirmedMsgs:
            return False
        
        lstBlck = self.blockchain.lastBlck

        msgs:str = ""
        for i in self.unconfirmedMsgs:
            msgs += i

        newBlck = Block(message = msgs,
                        timestamp = time.time(),
                        prvHash = lstBlck.hash,
                        index=lstBlck.id + 1,)
        
        proof = self.blockchain.pow(newBlck)
        self.blockchain.addBlck(newBlck, proof)
        self.unconfirmedMsgs = []

        self.currBlock = newBlck.id

    def addNewMsg(self, msg) -> None:
        """Api to add msg to queue"""
        self.unconfirmedMsgs.append(msg)

    def getQueueLength(self) -> int:
        """API to know length of current queue"""
        return len(self.unconfirmedMsgs)

    def PullMsgs(self) -> list:
        """Get new Msgs"""
        msgs = []
        if self.blockchain.lastBlck.id > self.currBlock:
            self.currBlock += 1
            msgs += self.blockchain.getBlock(self.currBlock).msg
        
        return msgs