import os
import sys
color = os.getenv("GENKI_STD_COLOR")
if color == 'ok':
	from portage.output import *
else:
	from nocolor import green, turquoise, white, red, yellow
import utils