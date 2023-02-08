import subprocess
import os

def create_vpn():
    # Définir les paramètres du VPN
    server_ip = "192.168.1.1"
    client_ip = "192.168.1.2"
    port = "1194"
    proto = "udp"

    # Créer le fichier de configuration du serveur
    with open("server.conf", "w") as f:
        f.write("dev tun\n")
        f.write("proto {}\n".format(proto))
        f.write("port {}\n".format(port))
        f.write("server {} 255.255.255.0\n".format(server_ip))
        f.write("push \"redirect-gateway def1\"\n")
        f.write("push \"dhcp-option DNS 8.8.8.8\"\n")
        f.write("keepalive 10 60\n")
        f.write("comp-lzo\n")
        f.write("persist-key\n")
        f.write("persist-tun\n")
        f.write("status openvpn-status.log\n")
        f.write("verb 3\n")

    # Créer le fichier de configuration du client
    with open("client.conf", "w") as f:
        f.write("client\n")
        f.write("dev tun\n")
        f.write("proto {}\n".format(proto))
        f.write("remote {} {}\n".format(server_ip, port))
        f.write("resolv-retry infinite\n")
        f.write("nobind\n")
        f.write("persist-key\n")
        f.write("persist-tun\n")
        f.write("comp-lzo\n")
        f.write("verb 3\n")

    # Lancer le serveur VPN
    subprocess.call(["openvpn", "--config", "server.conf"])

    # Lancer le client VPN
    subprocess.call(["openvpn", "--config", "client.conf"])

if __name__ == '__main__':
    create_vpn()
