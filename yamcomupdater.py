#This script checks the ip writes it into a file and if there's a change it updates the A entry on yay.com
#Rechecks every minute
import time
import requests
import subprocess
import json

def update():
    auth_header = {
        u'X-Auth-Reseller': u'XAUTHRESELLER',
        u'X-Auth-User': u'admin',
        u'X-Auth-Password': u'XAUTHPASSWORD'
    }

    data = {
        'priority': 0,
        'record_content': wanip,
        'record_name': 'DOMAIN NAME',
        'record_type': 'A',
        'ttl': TTL
    }

    r = requests.put(
        u'https://api.yay.com/dom/dns-zone/{zone_uuid}/record/{uuid}'.format(
            zone_uuid=u'DNS ZONE UUID',
            uuid=u'DNS ENTRY UUID'
        ),
        headers=auth_header,
        data=json.dumps(data)
    )

    print r.status_code
    print r.content

def check():
    global wanip
    wanip = subprocess.check_output('curl -s https://api.ipify.org', shell=True)
    wanip = wanip.strip()
    tailip = subprocess.check_output('tail -n 1 /opt/rawip.log', shell=True)
    tailip = tailip.strip()
    if tailip == wanip:
        print(tailip, "=", wanip)
    else:
        print("updating ip...")
        f = open("/opt/rawip.log", "w")
        f.write(wanip)
        update()
check()

while True:
    time.sleep(60)
    check()
