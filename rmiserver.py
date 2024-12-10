import Pyro4

@Pyro4.expose
class RemoteService():
    def func(self,name):
        print("Hello: ",name)

def server():

    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(RemoteService)
    ns.register("example.rmi",uri)

    print("Connected server 1")

    daemon.requestLoop()

server()
