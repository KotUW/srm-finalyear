from Api import serv

def test_SendingMsg():
    assert serv.PostMsg("This should be posted")

def test_PublishMsg():
    assert serv.SyncMsgs()

def test_GettheMsgback():
    a = serv.GetMsg()
    assert a[0] == "This should be posted"
    