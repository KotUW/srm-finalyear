from blockchain import Blockchain, Block

class MessageQueue:
    unconfirmedMsgs = []
    chain:Blockchain

    def __init__(self):
        chain = Blockchain
        chain.CreateGenesisBlock(1)

    def mine(self):
        """Basic Mining Function that go through any unconfirmed transactions and try to append them to the blockchain"""
        if not self.unconfirmedMsgs:
            return False
        
        lstBlck = self.chain.lastBlck

        newBlck = Block(index=lstBlck.index + 1, 
                        message = self.unconfirmedMsgs,
                        timestamp = time.time(),
                        prevHash = lstBlck.hash)
        
        proof = self.pow(newBlck)
        self.chain.addBlck(newBlck, proof)
        self.unconfirmedMsgs = []

        return newBlck.index

    
    def addNewMsg(self, msg) -> None:
        self.unconfirmedMsgs.append(msg)