import sys, os
from buildbot.buildslave import BuildSlave

class MySlaveBase(object):
    def extract_attrs(self, name, **kwargs):
        self.slavename = name
        remaining = {}
        for k in kwargs:
            if hasattr(self, k):
                setattr(self, k, kwargs[k])
            else:
                remaining[k] = kwargs[k]
        return remaining

    def get_pass(self, name):
        # get the password based on the name
        path = os.path.join(os.path.dirname(__file__), "%s.pass" % name)
        pw = open(path).read().strip()
        return pw

class MySlave(MySlaveBase, BuildSlave):
    def __init__(self, name, **kwargs):
        password = self.get_pass(name)
        kwargs = self.extract_attrs(name, **kwargs)
        BuildSlave.__init__(self, name, password, **kwargs)

slaves = [
    # Local
    MySlave('l1'),
    MySlave('mac')
]

# these are slaves that haven't been up and from whose owners I have not heard in a while
retired_slaves = [
]

def get_slaves(db=None, *args, **kwargs):
    rv = {}
    for arg in args:
        rv.update(arg)
    for sl in slaves:
        if db and db not in sl.databases:
            continue
        for k in kwargs:
            if getattr(sl, k) != kwargs[k]:
                break
        else:
            rv[sl.slavename] = sl
    return rv

def names(slavedict):
    return slavedict.keys()