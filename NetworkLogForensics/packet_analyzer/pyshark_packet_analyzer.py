import pyshark

#create a packet capture instance
#found the interface from cmd by using command 'tshark -D'
interface_selected = r'\Device\NPF_{0EBEC6C0-B28D-44DA-BACC-C9DE2774B12C}' #wifi interface

# capture = pyshark.LiveCapture(display_filter=' ip.addr == 192.186.0.100' , interface=interface_selected)

capture = pyshark.LiveCapture(interface=interface_selected)

capture.set_debug()

#start capturing the packets
capture.sniff(timeout=50)

#process captured packets
for packet in  capture:
    print(packet)

#stop the packet capture
capture.close()


# more resource (pyshark documentation) : https://pyshark-packet-analysis.readthedocs.io/en/latest/
