#!/usr/bin/python
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel,info
from mininet.topo import Topo
from mininet.link import Link, TCLink

def topology(Topo):
  net = Mininet(controller=RemoteController, link=TCLink, switch=OVSKernelSwitch)
  c0 = net.addController( 'c0', controller=RemoteController, ip='127.0.0.1', port=6633 )
  s1 = net.addSwitch('s1')
  s2 = net.addSwitch('s2')
  s3 = net.addSwitch('s3')
  s4 = net.addSwitch('s4')
  s5 = net.addSwitch('s5')
  h1 = net.addHost('h1', mac='00:00:00:00:00:01')
  net.addLink(s4, h1, bw=50)
  h2 = net.addHost('h2', mac='00:00:00:00:00:02')
  net.addLink(s2, h2, bw=50)
  h3 = net.addHost('h3', mac='00:00:00:00:00:03')
  net.addLink(s1, h3, bw=50)
  h4 = net.addHost('h4', mac='00:00:00:00:00:04')
  net.addLink(s3, h4, bw=50)
  h5 = net.addHost('h5', mac='00:00:00:00:00:05')
  net.addLink(s4, h5, bw=50)
  h6 = net.addHost('h6', mac='00:00:00:00:00:06')
  net.addLink(s4, h6, bw=50)
  h7 = net.addHost('h7', mac='00:00:00:00:00:07')
  net.addLink(s5, h7, bw=50)
  h8 = net.addHost('h8', mac='00:00:00:00:00:08')
  net.addLink(s1, h8, bw=50)
  h9 = net.addHost('h9', mac='00:00:00:00:00:09')
  net.addLink(s3, h9, bw=50)
  h10 = net.addHost('h10', mac='00:00:00:00:00:10')
  net.addLink(s4, h10, bw=50)
  net.addLink(s1, s2, bw=50)
  net.addLink(s1, s4, bw=50)
  net.addLink(s1, s5, bw=50)
  net.addLink(s2, s4, bw=50)
  net.addLink(s2, s5, bw=50)
  net.addLink(s3, s4, bw=50)
  net.addLink(s3, s5, bw=50)
  net.addLink(s4, s5, bw=50)
  net.build()
  c0.start()
  s1.start([c0])
  s2.start([c0])
  s3.start([c0])
  s4.start([c0])
  s5.start([c0])
  print('Start IPERF server')
  h1.cmdPrint('iperf -s -p 111 &')
  h2.cmdPrint('iperf -s -p 111 &')
  print('Create network and run simple performance test')
  print('Dumping host connections')
  dumpNodeConnections(net.hosts)
  for i in range (2):
   i=i+1
   print('###########START Test:%.2d###########'%i)
   h1.cmdPrint('iperf -c '+h1.IP()+' -p 111')
   h1.cmdPrint('iperf -c '+h2.IP()+' -p 111')
   h1.cmdPrint('ping -c3 ' + h2.IP())
   h1.cmdPrint('ping -c3 ' + h3.IP())

   print('###########Done Test:%.2d###########'%i)

topos = { 'mytopo': ( lambda: topology(Topo) ) }
if __name__ == '__main__':
  setLogLevel( 'info' )
  topology()
