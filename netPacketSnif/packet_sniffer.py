import sys
from scapy.all import sniff, get_if_list
from scapy.layers.inet import TCP, IP

def handle_packet(packet, log):
    if packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        log.write(f"TCP Connection: {src_ip}:{src_port} -> {dst_ip}:{dst_port}\n")

def main(interface, verbose=False):
    logfile_name = f"sniffer_{interface}_log.txt"
    with open(logfile_name, 'w') as logfile:
        try:
            if verbose:
                sniff(iface=interface, prn=lambda pkt: handle_packet(pkt, logfile), store=0, verbose=True)
            else:
                sniff(iface=interface, prn=lambda pkt: handle_packet(pkt, logfile), store=0)
        except KeyboardInterrupt:
            print("Sniffing stopped by user.")
            sys.exit(0)
        except Exception as e:
            print(f"Error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python packet_sniffer.py <interface> [verbose]")
        sys.exit(1)

    verbose = False
    if len(sys.argv) == 3 and sys.argv[2].lower() == "verbose":
        verbose = True

    interface = sys.argv[1]

    # Validate interface
    if interface not in get_if_list():
        print(f"Invalid interface: {interface}")
        sys.exit(1)

    main(interface, verbose)
