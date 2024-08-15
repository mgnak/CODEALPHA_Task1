**#TASK 4 - Network Intrusion Detection System**
Develop a network-based intrusion detection system using tools like Snort or Suricata.
Set up rules and alerts to identify and respond to suspicious network activity. You can even visualize the detected attacks.

**#Suricata**
Network Sniffer. Suricata is a high performance, open source network analysis and threat detection software used by most private and public organizations, and embedded by major vendors to protect their assets. 


Presentation and Working with Suricata
Presentation includes:

Use Cases Deployed.
Denial Of Service IDS - Detecting Denial of Service with the Help of Suricata Rules.
Raspberry Pi - Monitoring the Network and using IDS with RaspBerry Pi (Setup a Network with the help of switch, VM)
Firewall - We can even restrict access to a particular website

It is required that Suricata starts as root, however Suricata does have the ability to drop down to a non-root user after startup, which could limit the impact of a security vulnerability in Suricata itself.

Once Check the Security Considerations of Suricata, creating a seperate user andd giving permissions.

Rules of suricata are devided into 3 parts

Action: alert, drop, reject, pass, ...
Header / Protocol: tcp, udp, ...
Source and Destination: from where to where ...
Creating a rule: Navigate to /etc/suricata/rules > sudo nano rule_name.rules

breaking down: alert tcp any any -> any 23 (msg : 'TELNET CONNECTION ATTEMPTED'; sid: 1000001; rev:1;) alert is the action, tcp is the protocol we are monitoring any (1st occurence): is from the specified ip address (here any) any (2nd occurence): is from the specified port of the given ip(here any port of the given ip) any (3rd occurence): is to address if we are getting any packet from the specified ip and specified port 23 : to the provided port in the specified ip address sid: rule id 1000000 - 1999999 are for custom rules, rest for default rules rev: versions in the same rule.

Run Suricata:

-S for specifying the filename (the rules that should be followed)
-i (interface) we need to give which interface we are going to use (get it using ifconfig)
Command to run: suricata -S rule_name.rules -i eth0

We are good to go, suricata is all set(ignore any warnings or notices, they are not errors.)

Monitoring: Open /var/log/suricata

you can read the log file of suricata (connection and errors etc..) using > cat suricata.log
you can view the logs in live with the command > tail -f fast.log

Conclusion
I really had a great experience in dealing with Raspberry PI, creating my own rules for Suricata, and making IDS, DOS, Firewall which are minimal but gave me a lot of idea on how they work and how we can configure.
