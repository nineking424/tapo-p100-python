# python main2.py nineking424@gmail.com tjrxo424 192.168.0.48
from p110 import P110
import logging
import argparse

parser = argparse.ArgumentParser(description="Change plug state.")
parser.add_argument('tplink_email', metavar='TPLINK_EMAIL', type=str, help="Your TPLink account email")
parser.add_argument('tplink_password', metavar='TPLINK_PASS', type=str, help="Your TPLink account password")
parser.add_argument('address', metavar='ADDR', type=str, help="Address of your plug (ex. 192.168.2.22)")
parser.add_argument('new_state', metavar='STATE', type=int, help="New state of the plug (on=1 off=0) ")


args = parser.parse_args()


logger = logging.getLogger('root')
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.INFO)

logger.info(f"Will get state & energy of plug at '{args.address}'")

my_plug = P110(args.address)
my_plug.handshake()
my_plug.login_request(args.tplink_email, args.tplink_password)
state = my_plug.get_state()
logger.info(f"Returned result: {state}")

energy = my_plug.get_energy()
logger.info(f"Returned result: {energy}")

