#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller
from mininet.link import Link, TCLink
from mininet.log import setLogLevel

def simple_topology():
    net = Mininet(controller=Controller)
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    s1 = net.addSwitch('s1')
    
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    
    net.start()
    
    print("Network Interfaces:")
    for host in [h1, h2]:
        print(host.name, host.IP())
    
    print("Testing Connectivity:")
    net.pingAll()
    
    net.stop()

def linear_topology():
    net = Mininet(controller=Controller)
    hosts = []
    switches = []
    
    for i in range(3):
        host = net.addHost('h{}'.format(i+1))
        hosts.append(host)
        switch = net.addSwitch('s{}'.format(i+1))
        switches.append(switch)
        
        net.addLink(host, switch)
        if i > 0:
            net.addLink(switches[i-1], switch)
    
    net.start()
    
    print("Network Interfaces:")
    for host in hosts:
        print(host.name, host.IP())
    
    print("Testing Connectivity:")
    net.pingAll()
    
    net.stop()

def custom_topology():
    net = Mininet(controller=Controller)
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(h4, s2)
    net.addLink(s1, s2)
    
    net.start()
    
    print("Network Interfaces:")
    for host in [h1, h2, h3, h4]:
        print(host.name, host.IP())
    
    print("Testing Connectivity:")
    net.pingAll()
    
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    
    print("Simple Topology:")
    simple_topology()
    
    print("\nLinear Topology:")
    linear_topology()
    
    print("\nCustom Topology:")
    custom_topology()
