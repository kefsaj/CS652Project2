"""  
CS652 Project 2 Part 1: Fat-Tree Topology Generation

Modified By Kefin Sajan
Original: https://github.com/panandr/mininet-fattree/blob/master/fattree.py

Last Updated: 10/18/20

"""
import os
import logging
from mininet.topo import Topo


logging.basicConfig(filename='./fattree.record', level=logging.DEBUG)
logger = logging.getLogger(__name__)
"Logging for the whole process"

k = 4

class FatTree( Topo ):
  
    CoreSwitch  = []
    AggSwitch   = []
    EdgeSwitch  = []
    Host        = []
 
    def __init__( self, k):
        """
        
        Create Fat Tree topology
        
        """
        self.pod = k
        self.iCoreLayerSwitch = (k/2)**2
        self.iAggLayerSwitch = k*k/2
        self.iEdgeLayerSwitch = k*k/2
        self.density = k/2
        self.iHost = self.iEdgeLayerSwitch * self.density
        
        self.bw_c2a = 0.2
        self.bw_a2e = 0.1
        self.bw_h2a = 0.05

        # Init Topo
        Topo.__init__(self)
  
        self.createTopo()
        logger.debug("Finished topology creation!")

        self.createLink( bw_c2a=self.bw_c2a, 
                         bw_a2e=self.bw_a2e, 
                         bw_h2a=self.bw_h2a)
        logger.debug("Finished adding links!")

    #    self.set_ovs_protocol_13()
    #    logger.debug("OF is set to version 1.3!")  
    
    def createTopo(self):
        self.createCoreLayerSwitch(self.iCoreLayerSwitch)
        self.createAggLayerSwitch(self.iAggLayerSwitch)
        self.createEdgeLayerSwitch(self.iEdgeLayerSwitch)
        self.createHost(self.iHost)

### "   Create Switch "

    def _addSwitch(self, number, level, switch):
        for x in range(1, number+1):
            PREFIX = str(level) + "00"
            if x >= int(10):
                PREFIX = str(level) + "0"
            switch.append(self.addSwitch('s' + PREFIX + str(x)))

    def createCoreLayerSwitch(self, NUMBER):
        logger.debug("Create Core Layer")
        self._addSwitch(NUMBER, 1, self.CoreSwitch)

    def createAggLayerSwitch(self, NUMBER):
        logger.debug("Create Agg Layer")
        self._addSwitch(NUMBER, 2, self.AggSwitch)

    def createEdgeLayerSwitch(self, NUMBER):
        logger.debug("Create Edge Layer")
        self._addSwitch(NUMBER, 3, self.EdgeSwitch)

### "   Create Host "

    def createHost(self, NUMBER):
        logger.debug("Create Host")
        for x in range(1, NUMBER+1):
            PREFIX = "h00"
            if x >= int(10):
                PREFIX = "h0"
            elif x >= int(100):
                PREFIX = "h"
            self.Host.append(self.addHost(PREFIX + str(x)))

### "   Creation of Links   "

    def createLink(self, bw_c2a=0.2, bw_a2e=0.1, bw_h2a=0.5):
        logger.debug("Add link Core to Agg.")
        end = self.pod/2
        for x in range(0, self.iAggLayerSwitch, end):
            for i in range(0, end):
                for j in range(0, end):
                    linkopts = dict(bw=bw_c2a) 
                    self.addLink(
                        self.CoreSwitch[i*end+j],
                        self.AggSwitch[x+i],
                        **linkopts)

        logger.debug("Add link Agg to Edge.")
        for x in range(0, self.iAggLayerSwitch, end):
            for i in range(0, end):
                for j in range(0, end):
                    linkopts = dict(bw=bw_a2e) 
                    self.addLink(
                        self.AggSwitch[x+i], self.EdgeSwitch[x+j],
                        **linkopts)

        logger.debug("Add link Edge to Host.")
        for x in range(0, self.iEdgeLayerSwitch):
            for i in range(0, self.density):
                linkopts = dict(bw=bw_h2a) 
                self.addLink(
                    self.EdgeSwitch[x],
                    self.Host[self.density * x + i],
                    **linkopts)
        
topos = { 'fattree' : ( lambda k : FatTree(k)) }

