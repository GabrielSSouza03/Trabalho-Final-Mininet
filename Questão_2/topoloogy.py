#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info

class CustomTopo(Topo):
    def build(self):
        # Criação dos hosts
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')
        h4 = self.addHost('h4', ip='10.0.0.4/24')
        h5 = self.addHost('h5', ip='10.0.0.5/24')

        # Criação dos switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Criação dos links com 30 Mbps
        self.addLink(h1, s1, bw=30)
        self.addLink(h2, s1, bw=30)
        self.addLink(s1, s2, bw=30)
        self.addLink(s2, s3, bw=30)
        self.addLink(h3, s2, bw=30)
        self.addLink(h4, s3, bw=30)
        self.addLink(h5, s3, bw=30)

def run():
    topo = CustomTopo()
    net = Mininet(topo=topo, controller=None, link=TCLink, switch=OVSSwitch)
    net.start()

    info('*** Rede iniciada!\n')
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
