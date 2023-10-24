from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller
from mininet.cli import CLI

def create_and_run_topology(topo, controller=None):
    net = Mininet(topo=topo, switch=OVSSwitch, controller=controller)
    net.start()
    CLI(net)
    net.stop()

# Simple Topology
simple_topo = Mininet()
h1 = simple_topo.addHost('h1')
h2 = simple_topo.addHost('h2')
h3 = simple_topo.addHost('h3')
s1 = simple_topo.addSwitch('s1')
simple_topo.addLink(h1, s1)
simple_topo.addLink(h2, s1)
simple_topo.addLink(h3, s1)
create_and_run_topology(simple_topo)

# Linear Topology
linear_topo = Mininet()
h1 = linear_topo.addHost('h1')
h2 = linear_topo.addHost('h2')
h3 = linear_topo.addHost('h3')
s1 = linear_topo.addSwitch('s1')
s2 = linear_topo.addSwitch('s2')
s3 = linear_topo.addSwitch('s3')
linear_topo.addLink(h1, s1)
linear_topo.addLink(h2, s2)
linear_topo.addLink(h3, s3)
linear_topo.addLink(s1, s2)
linear_topo.addLink(s2, s3)
create_and_run_topology(linear_topo)

# Custom Tree Topology
custom_tree_topo = Mininet()
h1 = custom_tree_topo.addHost('h1')
h2 = custom_tree_topo.addHost('h2')
h3 = custom_tree_topo.addHost('h3')
s1 = custom_tree_topo.addSwitch('s1')
s2 = custom_tree_topo.addSwitch('s2')
s3 = custom_tree_topo.addSwitch('s3')
s4 = custom_tree_topo.addSwitch('s4')
custom_tree_topo.addLink(h1, s1)
custom_tree_topo.addLink(h2, s2)
custom_tree_topo.addLink(h3, s3)
custom_tree_topo.addLink(s1, s4)
custom_tree_topo.addLink(s2, s4)
custom_tree_topo.addLink(s3, s4)
create_and_run_topology(custom_tree_topo)
