from Api import serv

s = serv()

def test_SendingMsg():
    assert s.PostMsg("This should be posted")

def test_PublishMsg():
    assert s.SyncMsgs()

def test_GettheMsgback():
    a = s.GetMsg()
    assert a[0] == "This should be posted"
    