"""    
CS652 Project 2 Part 2: Fat-Tree Routing Protocol
By Kefin Sajan

Last Updated: 10/15/20

"""
#!/usr/bin/python

from mininet.node import CPULimitedHost
from mininet.node import Host
from mininet.node import Node
from mininet.node import OVSKernelSwitch
from mininet.topo import Topo

class fatTreeTopo(Topo):

    "Fat Tree Topology"

    def __init__(self):
        "Create Fat tree Topology"

        Topo.__init__(self)

#Add hosts
        h1 = self.addHost('h1', cls=Host, ip='10.0.1.1', defaultRoute=None)
        h2 = self.addHost('h2', cls=Host, ip='10.0.1.2', defaultRoute=None)
        h3 = self.addHost('h3', cls=Host, ip='10.0.1.3', defaultRoute=None)
        h4 = self.addHost('h4', cls=Host, ip='10.0.1.4', defaultRoute=None)
        
        h5 = self.addHost('h5', cls=Host, ip='10.0.2.5', defaultRoute=None)
        h6 = self.addHost('h6', cls=Host, ip='10.0.2.6', defaultRoute=None)
        h7 = self.addHost('h7', cls=Host, ip='10.0.2.7', defaultRoute=None)
        h8 = self.addHost('h8', cls=Host, ip='10.0.2.8', defaultRoute=None)
        
        h11 = self.addHost('h11', cls=Host, ip='10.0.3.1', defaultRoute=None)
        h12 = self.addHost('h12', cls=Host, ip='10.0.3.2', defaultRoute=None)
        h13 = self.addHost('h13', cls=Host, ip='10.0.3.3', defaultRoute=None)
        h14 = self.addHost('h14', cls=Host, ip='10.0.3.4', defaultRoute=None)
        
        h15 = self.addHost('h15', cls=Host, ip='10.0.4.5', defaultRoute=None)
        h16 = self.addHost('h16', cls=Host, ip='10.0.4.6', defaultRoute=None)
        h17 = self.addHost('h17', cls=Host, ip='10.0.4.7', defaultRoute=None)
        h18 = self.addHost('h18', cls=Host, ip='10.0.4.8', defaultRoute=None

#Add switches
    ### Edge Switches
        s1  = self.addSwitch('s1' , cls=OVSKernelSwitch)
        s2  = self.addSwitch('s2' , cls=OVSKernelSwitch)
        s3  = self.addSwitch('s3' , cls=OVSKernelSwitch)
        s4  = self.addSwitch('s4' , cls=OVSKernelSwitch)
        
        s5  = self.addSwitch('s5', cls=OVSKernelSwitch)
        s6  = self.addSwitch('s6', cls=OVSKernelSwitch)
        s7  = self.addSwitch('s7', cls=OVSKernelSwitch)
        s8  = self.addSwitch('s8', cls=OVSKernelSwitch)

    ### Aggregation Switch
        s9  = self.addSwitch('s9', cls=OVSKernelSwitch)
        s10 = self.addSwitch('s10', cls=OVSKernelSwitch)
        s11 = self.addSwitch('s11', cls=OVSKernelSwitch)
        s12 = self.addSwitch('s12', cls=OVSKernelSwitch)

        s13 = self.addSwitch('s13' , cls=OVSKernelSwitch)
        s14 = self.addSwitch('s14' , cls=OVSKernelSwitch)
        s15 = self.addSwitch('s15', cls=OVSKernelSwitch)
        s16 = self.addSwitch('s16', cls=OVSKernelSwitch)

    ### Core Switches
        s21  = self.addSwitch('s21' , cls=OVSKernelSwitch)
        s22  = self.addSwitch('s22' , cls=OVSKernelSwitch)
        s23  = self.addSwitch('s23' , cls=OVSKernelSwitch)
        s24  = self.addSwitch('s24' , cls=OVSKernelSwitch)
        
#Add links
    ### Add Edge
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)

        self.addLink(h5, s3)
        self.addLink(h6, s3)
        self.addLink(h7, s4)
        self.addLink(h8, s4)

        self.addLink(h11, s5)
        self.addLink(h12, s5)
        self.addLink(h13, s6)
        self.addLink(h14, s6)

        self.addLink(h15, s7)
        self.addLink(h16, s7)
        self.addLink(h17, s8)
        self.addLink(h18, s8)

    ### Add Aggregation
        self.addLink(s1, s9)
        self.addLink(s1, s10)
        self.addLink(s2, s10)
        self.addLink(s2, s9)

        self.addLink(s3, s11)
        self.addLink(s4, s11)
        self.addLink(s3, s12)
        self.addLink(s4, s12)

        self.addLink(s5, s13)
        self.addLink(s6, s13)
        self.addLink(s5, s14)
        self.addLink(s6, s14)

        self.addLink(s7, s15)
        self.addLink(s8, s15)
        self.addLink(s7, s16)
        self.addLink(s8, s16)

    ### Add Core
        self.addLink(s7, s15)
        self.addLink(s8, s15)
        self.addLink(s7, s16)
        self.addLink(s8, s16)

        self.addLink(s21, s9)
        self.addLink(s21, s11)
        self.addLink(s21, s13)
        self.addLink(s21, s15)

        self.addLink(s22, s9)
        self.addLink(s22, s11)
        self.addLink(s22, s13)
        self.addLink(s22, s15)

        self.addLink(s23, s10)
        self.addLink(s23, s12)
        self.addLink(s23, s14)
        self.addLink(s23, s16)

        self.addLink(s24, s10)
        self.addLink(s24, s12)
        self.addLink(s24, s14)
        self.addLink(s24, s16)



topos = { 'mytopo': (lambda: fatTreeTopo() ) }