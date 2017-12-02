python ovxctl.py -n createNetwork tcp:localhost:20000 10.0.0.0 16
python ovxctl.py -n createSwitch 2 00:00:00:00:00:00:01:00
python ovxctl.py -n createSwitch 2 00:00:00:00:00:00:02:00
python ovxctl.py -n createSwitch 2 00:00:00:00:00:00:03:00
python ovxctl.py -n createPort 2 00:00:00:00:00:00:01:00 3
python ovxctl.py -n createPort 2 00:00:00:00:00:00:01:00 5
python ovxctl.py -n createPort 2 00:00:00:00:00:00:02:00 5
python ovxctl.py -n createPort 2 00:00:00:00:00:00:02:00 6
python ovxctl.py -n createPort 2 00:00:00:00:00:00:03:00 5
python ovxctl.py -n createPort 2 00:00:00:00:00:00:03:00 4
python ovxctl.py -n connectLink 2 00:a4:23:05:00:00:00:01 2 00:a4:23:05:00:00:00:02 1 spf 1
python ovxctl.py -n connectLink 2 00:a4:23:05:00:00:00:02 2 00:a4:23:05:00:00:00:03 1 spf 1
python ovxctl.py -n connectHost 2 00:a4:23:05:00:00:00:01 1 00:00:00:00:01:03
python ovxctl.py -n connectHost 2 00:a4:23:05:00:00:00:03 2 00:00:00:00:03:04
python ovxctl.py -n startNetwork 2
