from multiprocessing.dummy import Array
from MessageQueue import MessageQueue as MQ

class serv:
    msgQ = MQ

    def PostMsg(self, msg:str) -> bool:
        """Post a Messgae"""
        raise NotImplementedError()

    def SyncMsgs(self) -> bool:
        """Publish to blockchain"""
        raise NotImplementedError()

    def GetMsg(self) -> list:
        """Get all the msg the user has missed"""
        raise NotImplementedError()