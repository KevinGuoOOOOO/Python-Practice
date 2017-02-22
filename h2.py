import re

with open('test.txt', 'r') as f:
    lines = f.readlines()

results = {}
for line in lines:
    if "configiso.pl" in line and "RESPONSE" not in line:
        # 20:06:51 	URL: http://nbapppxe.engba.veritas.com/cgi-bin/xgeo/configiso.pl?site=CD-B5214&model=5230&hosttype=HARDWARE&hostname=i9-eng142&isotype=main
        m = re.search('^\s*(?P<time>\S*).*hostname=(?P<hostname>.*?)&', line)
        if m:
            hostname = m.group('hostname')
            if hostname not in results:
                results[hostname] = {'start':'', 'end':'', 'elapsed':''}
            results[hostname]['start'] = m.group('time')

    if "Installation on" in line and "successful" in line:
        # 21:08:19 Installation on i97-eng142 successful
        m = re.search('^\s*(?P<time>\S*) Installation on (?P<hostname>\S*) successful', line)
        if m:
            hostname = m.group('hostname')
            results[hostname]['end'] = m.group('time')

import json
print json.dumps(results, indent=2)
