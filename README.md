# Plug P100
This is a fork of original work of [@K4CZP3R](https://github.com/K4CZP3R/tapo-p100-python)

**The purpose of this fork is support for the P110.**

# How to use it(P100)
```
usage: main.py [-h] TPLINK_EMAIL TPLINK_PASS ADDR STATE

Change plug state.

positional arguments:
  TPLINK_EMAIL  Your TPLink account email
  TPLINK_PASS   Your TPLink account password
  ADDR          Address of your plug (ex. 192.168.2.22)
  STATE         New state of the plug (on=1 off=0)

optional arguments:
  -h, --help    show this help message and exit
```

Example: `python main.py email@gmail.com Password123 192.168.137.135 1`


# How to use it(P110)
```
usage: main2.py [-h] TPLINK_EMAIL TPLINK_PASS ADDR

Get device info & Energy usage

positional arguments:
  TPLINK_EMAIL  Your TPLink account email
  TPLINK_PASS   Your TPLink account password
  ADDR          Address of your plug (ex. 192.168.2.22)

optional arguments:
  -h, --help    show this help message and exit
```

Example: `python main2.py email@gmail.com Password123 192.168.137.135`
