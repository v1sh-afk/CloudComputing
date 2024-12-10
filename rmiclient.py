import Pyro4

def client():
    remote_serive = Pyro4.Proxy("PYRONAME:example.rmi")
    remote_serive.func("Name")

client()