import time
from siemens.pac import PACx200

times = []

p = PACx200('192.168.1.5')
while True:
    try:
        p.read()
        print(p.as_dict(replace_nan=True))
    except:
        break
    time.sleep(1)
