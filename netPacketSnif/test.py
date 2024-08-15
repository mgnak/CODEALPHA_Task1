# from scapy.all import get_if_list
#
# # Print all available network interfaces
# print("Available network interfaces:")
# for iface in get_if_list():
#     print(iface)


from scapy.all import sniff


def packet_callback(packet):
    print(packet.summary())


sniff(prn=packet_callback, count=10)
