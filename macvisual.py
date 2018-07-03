#!/usr/bin/env python

""" macvisual.py

Author: Anthony Panisales

- Reads in a pcap file and creates a directed graph with the nodes 
  representing MAC addresses and the edges representing packets. If 
  a node has an edge pointing to another node, then that means that 
  a packet has been sent from that node's MAC address to the MAC address 
  at the node that the edge is pointing to.

- Usage: python macvisual.py pcap_file

- References:
	http://dpkt.readthedocs.io/en/latest/_modules/examples/print_packets.html
	https://networkx.github.io/documentation/stable/tutorial.html
	http://www.commercialventvac.com/dpkt.html

"""

from __future__ import print_function
from future.utils import python_2_unicode_compatible
from dpkt.compat import compat_ord
import dpkt
import matplotlib.pyplot as plt
import networkx as nx
import sys


def main():
	try:
		pcap = dpkt.pcap.Reader(open(sys.argv[1],'rb'))
	except (IOError, IndexError, ValueError):
		print("Error: A pcap file could not be read")
		sys.exit()

	DG = nx.DiGraph()

	for ts, pkt in pcap:
	    eth = dpkt.ethernet.Ethernet(pkt)
	    srcMac = ':'.join('%02x' % compat_ord(b) for b in eth.src)
	    dstMac = ':'.join('%02x' % compat_ord(b) for b in eth.dst)
	    DG.add_edge(srcMac, dstMac)

	nx.draw(DG, with_labels=True, node_color='skyblue')
	plt.draw()
	plt.show()

if __name__ == '__main__':
	main()
