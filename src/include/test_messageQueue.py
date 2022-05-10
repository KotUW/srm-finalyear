from MessageQueue import *

MQ = MessageQueue()

def test_addMsGToQueue():
    assert MQ.addNewMsg("This is love") == None
    
def test_NumberOfMesgs():
    MQ.addNewMsg("First line")
    assert MQ.getQueueLength() == 1

def test_Pushing():
    MQ.addNewMsg("This is Life")
    assert not MQ.PushMsgs() == None

