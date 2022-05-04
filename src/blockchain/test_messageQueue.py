from MessageQueue import *

MQ = MessageQueue()

def test_addMsGToQueue():
    assert MQ.addNewMsg("This is love") == None
    

def test_mining():
    MQ.addNewMsg("This is Life")
    assert not MQ.mine() == None