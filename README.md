# simplemininet
A simple mininet script attached to SDN controller with 5 switches and 10 hosts to performed simple network performance test that loop 2 times. By default the ip address for the controller is 127.0.0.l. Change it if necessary. Modify the script for more added host to be included in the test.

Use this mininet command to execute the script:

sudo -S mn -c && sudo mn --custom 5s-10h.py --topo=mytopo --controller=remote --test none
