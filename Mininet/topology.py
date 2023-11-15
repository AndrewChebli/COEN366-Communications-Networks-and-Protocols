from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info


def topology():
    net = Mininet(controller=Controller, switch=OVSSwitch, waitConnected=True)

    info("adding a controller c0\n")
    c0 = net.addController("c0")

    info("adding the switches s1,s2,s3\n")
    s1 = net.addSwitch("s1")
    s2 = net.addSwitch("s2")
    s3 = net.addSwitch("s3")

    info("creating the hosts\n")
    h1 = net.addHost("h1", ip="127.0.0.2")
    h2 = net.addHost("h2", ip="127.0.0.3")
    h3 = net.addHost("h3", ip="127.0.0.4")

    # to link the switches together
    net.addLink(s1, s2)
    net.addLink(s1, s3)
    net.addLink(s2, s3)

    # to link hosts to switches
    net.addLink(h1, s1)
    net.addLink(h2, s2)
    net.addLink(h3, s3)

    info("Starting the network\n")
    net.start()

    info("pinging the network\n")

    net.pingAll()

    info("opening cli")
    CLI(net)

    info("stopping the network")
    net.stop()


if __name__ == "__main__":
    setLogLevel("info")
    topology()
