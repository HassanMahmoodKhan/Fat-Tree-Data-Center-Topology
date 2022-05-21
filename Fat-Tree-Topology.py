from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.link import TCLink
from mininet.util import dumpNetConnections

class MyTopo(Topo):

    def __init__(self):
        super(MyTopo, self).__init__()

        #Number of swtiches per layer
        k = 2
        pod = k
        L1 = (pod//2)**2
        L2 = pod*pod//2 
        L3 = L2

        #Creating switches
        c = [] #core layer switches
        a = [] #aggregation layer swtiches
        e = [] #edge layer switches

        #Add swicthes
        for i in range (L1):
             c_sw = self.addSwitch('c{}'.format(i+1))    #Label runs form 1 to n
             c.append(c_sw)

        for i in range (L2):
            a_sw = self.addSwitch('a{}'.format(L1+i+1))
            a.append(a_sw)    
            

        for i in range (L3):
           e_sw = self.addSwitch('e{}'.format(L1+L2+i+1))
           e.append(e_sw)      
            

        #Creating links between switches
        #The core layer and aggregation layer links
        for i in range(L1):
            c_sw = c[i]
            start = i%(pod//2)
            for j in range(pod):
                self.addLink(c_sw,a[start+j*(pod//2)],bw=10)

        #aggregation and edge layer links
        for i in range(L2):
            group = i//(pod//2)
            for j in range(pod//2):
                self.addLink(a[i],e[group*(pod//2)+j],bw=10)

        #Creating hosts and adding links between switches and hosts
        for i in range(L3):
            for j in range(2):
                hs = self.addHost('h{}'.format(i*2+j+1),bw=10)
                self.addLink(e[i],hs)

topos = {"mytopo":(lambda:MyTopo())}
