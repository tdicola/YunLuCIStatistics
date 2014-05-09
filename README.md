YunLuCIStatistics
=================

Graph data from an Arduino Yun on its LuCI web console.

Setup
-----

0.  As a pre-step make sure you have an SD card and have expanded the Yun filesystem following [these steps](http://blog.arduino.cc/2014/05/06/time-to-expand-your-yun-disk-space-and-install-node-js/) before proceeding.

1.  Connect to your Yun over SSH and execute the following commands:

    ````
    opkg update
    opkg install luci-app-statistics
    opkg install collectd-mod-exec
    ````

2.  Copy CollectdYunConsole.py to the Yun using SCP.  Run this from your computer:

    ````
    scp CollectdYunConsole.py root@arduino.local:/root
    ````

3.  Copy exec.lua to the Yun.  This must be installed in a specific spot for LuCI:

    ````
    scp exec.lua root@arduino.local:/usr/lib/lua/luci/statistics/rrdtool/definitions/exec.lua
    ````

4.  Access the LuCI web console by navigating to http://arduino.local -> Configure -> advanced configuration panel (luci)

5.  Click the 'Statistics' tab at the top of the screen.

6.  Click the 'Collectd' sub-tab to go to the collectd configuration.

7.  Navigate to the 'System Plugins' -> 'Exec' sub-tab.

8.  Check the 'Enable this plugin' box.  Under 'Add command for reading values' click 'Add' and enter the following values:
    -   Script: python -u /root/CollectdYunConsole.py
    -   User: nobody
    -   Group: nogroup

9.  Click 'Save & Apply' at the bottom of the screen.

10. Restart your Yun to make sure all the changes are applied and loaded.

11. Once restarted, load a sketch on the Yun such as the provided YunTestSensor sketch.  To send values to be graphed, initialize the Console class and write lines of output of the form "name:value" to the Console.  Name can be any string value, and value must be an integer or float value.  By default collectd will gather stats every 30 seconds, so delay at least 10 seconds or so between measurements.  You can change the time for collection in the collectd settings in LuCI.

12. Open LuCI again, then navigate to the 'Statistics' -> 'Graphs' -> 'Exec' tab.  Your sensor charts should be displayed!

13. Note by default the graph data will be completely removed on reboot.  You can have the data saved by changing the location of the RRD database which stores meaursements from the default /tmp location to a new location such as /mnt/sda1/rrd on the SD card.  Navigage to 'Statistics' -> 'Collectd' -> 'Output plugins' and change the 'Storage directory' setting.