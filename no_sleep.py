import win32api, win32con
import time
import random

# There is a side effect. Some applications interpret these as a backspace key
keys = {
    'F15': 0x7E,
    'F16': 0x7F,
    'F17': 0x80,
    'F18': 0x81,
    'F19': 0x82
}

def key_press(key):
    win32api.keybd_event(key, 0,0,0)
    rand_time = random.randint(1, 7)
    time.sleep(rand_time/100)
    win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)


interval_max = 59
interval_min = 40

while True:
    time.sleep(random.randint(interval_min, interval_max))
    random_key = random.choice(list(keys.values()))
    key_press(random_key)
