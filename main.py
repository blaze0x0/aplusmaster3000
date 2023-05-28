import os
import sys

import core.local
import core.log

print(core.local.logo)
core.log.meta(core.local.version)

if not os.path.exists(core.local.ppath):
    core.log.error("Please input prompt in " + core.local.ppath)
    sys.exit()

with open(core.local.ppath, "r") as f:
    assignment = f.read()

print(assignment)