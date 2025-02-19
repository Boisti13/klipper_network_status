# Original: https://github.com/JeremyRuhland/klipper_network_status
# Test
import os, logging, sys

class network_status:
    def __init__(self, config):
        self.interval = config.getint('interval', 60, minval=10)
        self.ethip = "N/A"
        self.zeroip = "N/A"
        self.wifiip = "N/A"
        self.wifissid = "N/A"
        self.mdns = "N/A"
        self.last_eventtime = 0

    def get_status(self, eventtime):
        if eventtime - self.last_eventtime > self.interval:
            self.last_eventtime = eventtime
            logging.info("network_status get_status %d" % eventtime)
            try:
                self.ethip = os.popen('ip addr show eth0').read().split("inet ")[1].split("/")[0]
            except:
                self.ethip = "N/A"

            try:
                self.zeroip = os.popen('ip addr show ztrf2zupaa').read().split("inet ")[1].split("/")[0]
            except:
                self.zeroip = "N/A"
                
            try:
                self.wifiip = os.popen('ip addr show wlan0').read().split("inet ")[1].split("/")[0]
                self.wifissid = os.popen('iwgetid -r').read()[:-1]
            except:
                self.wifiip = "N/A"
                self.wifissid = "N/A"

            self.mdns = os.popen('hostname').read()[:-1] + '.local'

        return {'ethip': self.ethip,
            'zeroip' : self.zeroip,
            'wifiip': self.wifiip,
            'wifissid': self.wifissid,
            'mdns': self.mdns}

def load_config(config):
    return network_status(config)

def manage_zerotier(action):
    if action not in ["start", "stop", "restart", "status"]:
        print("Invalid action. Use 'start', 'stop', 'restart', or 'status'.")
        return

    os.system(f"sudo systemctl {action} zerotier-one")

# Check if an argument is provided
    if len(sys.argv) != 2:
        print("Usage: python3 manage_zerotier.py <action>")
    else:
        action = sys.argv[1]
    manage_zerotier(action)