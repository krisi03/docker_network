from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel
import random

class CustomTopo(Topo):
    def build(self):
        # Add 519 switches
        switches = []
        for i in range(519):
            switch = self.addSwitch(f's{i+1}')
            switches.append(switch)
        
        # Add 15 hosts and connect them to random switches
        for i in range(15):
            host = self.addHost(f'h{i+1}')
            switch = random.choice(switches)
            self.addLink(host, switch)
        
        # Connect all switches in a linear topology for simplicity
        for i in range(518):
            self.addLink(switches[i], switches[i+1])
           
           
topos = { 'mytopo': ( lambda: CustomTopo() ) }
    
def run():
    topo = CustomTopo()
    controller=RemoteController('c0', ip='127.0.0.1', port=6653)
    net = Mininet(topo=topo,controller=controller)
    net.start()
    CLI(net)
    net.stop()