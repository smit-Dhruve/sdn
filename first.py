#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller
from mininet.link import Link, TCLink
from mininet.log import setLogLevel

def create_topology(host_count, switch_count, links_per_switch):
    net = Mininet(controller=Controller)
    hosts = []
    switches = []
    
    for i in range(host_count):
        host = net.addHost('h{}'.format(i+1))
        hosts.append(host)
    
    for i in range(switch_count):
        switch = net.addSwitch('s{}'.format(i+1))
        switches.append(switch)
        
        for j in range(links_per_switch):
            net.addLink(switches[i], hosts[links_per_switch * i + j])
    
    net.start()
    
    print("Network Interfaces:")
    for host in hosts:
        print(host.name, host.IP())
    
    print("Testing Connectivity:")
    net.pingAll()
    
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    
    print("Simple Topology:")
    create_topology(2, 1, 2)
    
    print("\nLinear Topology:")
    create_topology(4, 4, 1)
    
    print("\nTree Topology:")
    create_topology(5, 5, 2)
