from mininet.net import Mininet
from mininet.topo import Topo
from mininet.cli import CLI

class CustomTreeTopo(Topo):
    def build(self, depth=2, fanout=2):
        # Create the root switch
        root_switch = self.addSwitch('s1')

        # Recursive function to create tree-like structure
        def add_tree_links(node, current_depth):
            if current_depth == depth:
                return
            for i in range(fanout):
                child_switch = self.addSwitch('s%s' % (len(self.switches) + 1))
                self.addLink(node, child_switch)
                add_tree_links(child_switch, current_depth + 1)

        # Start building the tree
        add_tree_links(root_switch, 0)

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

# Custom Tree Topology
custom_tree_topo = CustomTreeTopo(depth=2, fanout=2)
create_and_run_topology(custom_tree_topo)

