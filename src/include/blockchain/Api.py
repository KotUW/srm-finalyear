from MessageQueue import MessageQueue as MQ


# TODO Mege into Message Queue
class serv:
    msgQ = MQ()
    currBlock = 0

    def PostMsg(self, msg:str) -> bool:
        """Post a Messgae"""
        if self.msgQ.addNewMsg(msg) == None:
            return True
        return False

    def PushMsgs(self) -> bool:
        """Publish to blockchain"""
        tmp = self.currBlock
        self.currBlock = self.msgQ.mine()

        if self.currBlock > tmp:
            return True
        return False

    def PullMsgs(self) -> list:
        """Synced to the current chain."""
        currBlck = self.msgQ.chain.chain.lastBlck.id
        msgs = []
        if currBlck > self.currBlock:
            while (self.currBlock < currBlck):
                msgs.append(self.GetMsg(self.currBlock))
        
        if len(msgs) > 0:
            return msgs
        return None
    
    def GetMsg(self, blckId:int) -> str:
        """Get all the msg the user has missed"""
        
