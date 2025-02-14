import os, requests as req
def test_reverse():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/amarotta/reverse"
    
    r = {"input" : "pippo"}
    res = req.post(url, json=r ).json()
    
    assert res.get("output") == "oppip"
