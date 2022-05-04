from multiprocessing.dummy import Array
from MessageQueue import MessageQueue as MQ

class serv:
    msgQ = MQ()
    currBlock = 0

    def PostMsg(self, msg:str) -> bool:
        """Post a Messgae"""
        if self.msgQ.addNewMsg(msg) == None:
            return True
        return False

    def SyncMsgs(self) -> bool:
        """Publish to blockchain"""
        tmp = self.currBlock
        self.currBlock = self.msgQ.mine()

        if self.currBlock > tmp:
            return True
        return False

    def GetMsg(self) -> list:
        """Get all the msg the user has missed"""
        raise NotImplementedError()