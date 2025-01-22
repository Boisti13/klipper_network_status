Klipper Network Status Plugin
=============================

Allow gcode macros to access system IP/hostname/wifi SSID/etc.

To install this plugin, clone repo into your rpi home folder and run `install.sh`.

```
git clone https://github.com/boisti13/klipper_network_status
```

```
./klipper_network_status/install.sh
```

You may also add the following to your moonraker configuration:

```
[update_manager client klipper_network_status]
type: git_repo
path: /home/pi/klipper_network_status
origin: https://github.com/Boisti13/klipper_network_status
install_script: install.sh
```

Then, add `[network_status]` somewhere in your klipper configuration to enable
the plugin.

You are now able to access information about the printer's network interfaces
from within macros or display fields. For example, add the following to your
menu override file to create a sub-list called "Network":

```
[menu __main __network]
type: list
name: Network

[menu __main __network _mdns]
type: command
name: mDNS: {printer.network_status.mdns}

[menu __main __network __ethernet]
type: list
name: Ethernet

[menu __main __network __ethernet _ethip]
type: command
name: {printer.network_status.ethip}

[menu __main __network __wifi]
type: list
name: Wifi

[menu __main __network __wifi _wifissid]
type: command
name: Wifi SSID: {printer.network_status.wifissid}

[menu __main __network __wifi _wifiip]
type: command
name: {printer.network_status.wifiip}

[menu __main __network __zerotier]
type: list
name: Zerotier

[menu __main __network __zerotier _zeroip]
type: command
name: {printer.network_status.zeroip}
```

I find that the text can be a little long for smaller displays so it may help
readability to put the actual hostname or IP address on its own line. It should
scroll side to side when the selection cursor hovers over it.

Optionally you can add an `interval` parameter to your klipper config under the `[network_status]` section to select how often the network information is updated. Default is once per minute if you do not specify.
