from Api import serv

s = serv()

def test_SendingMsg():
    assert s.PostMsg("This should be posted")

def test_PublishMsg():
    s.PostMsg("This is for you love")
    assert s.SyncMsgs()

def test_Pullmsgs():
    test_PublishMsg()
    assert isinstance(s.PullMsgs, list)

def test_GettheMsgback():
    a = s.GetMsg()
    assert a[0] == "This should be posted"
    