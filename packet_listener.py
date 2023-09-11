import scapy.all as scapy
from scapy_http import http

def listen_packets(interface):

    scapy.sniff(iface=interface,store=False,prn=analyze_packets) #gelen paketleri dinlemek. store=false patkeri kaydetme.
    #prn = callback function #paketleri kaydedeceği yer.

def analyze_packets(packet):
    #packet.show()
    if packet.haslayer(http.HTTPRequest):  #http altında http request var mı ?
        if packet.haslayer(scapy.Raw):     #scapy ile raw katmanınına gideriz.
            print(packet[scapy.Raw].load)  #scapy ile raw katmanında olan loadı yazdrırır.

listen_packets("eth0")
