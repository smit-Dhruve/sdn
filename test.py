from mininet.net import Mininet
from mininet.topo import SingleSwitchTopo, LinearTopo, TreeTopo
from mininet.cli import CLI

def create_and_run_topology(topo, controller=None):
    net = Mininet(topo=topo, controller=controller)
    net.start()
    CLI(net)
    net.stop()

# Simple Topology
simple_topo = SingleSwitchTopo(3)
create_and_run_topology(simple_topo)

# Linear Topology
linear_topo = LinearTopo(3)
create_and_run_topology(linear_topo)

# Tree Topology
tree_topo = TreeTopo(depth=2, fanout=2)
create_and_run_topology(tree_topo)
