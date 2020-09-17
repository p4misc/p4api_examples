from P4 import P4,P4Exception
import os
import re
import inspect
import config

p4 = P4()
p4.port = config.P4PORT
p4.user = config.P4USER
p4.client = config.P4CLIENT

try:
  p4.connect()

  # p4 workspace -o 
  workspace = p4.fetch_workspace(p4.client)

  # p4 filelog ...
  depotFiles = p4.run_filelog( workspace['Root'] + "\\..." )

  for file in depotFiles:
    print(file.depotFile)
    for revision in file.revisions:
      print("	%s %s#%s@%s <%s> by %s at %s" % (revision.action,revision.depotFile,revision.rev,revision.change,revision.type,revision.user,revision.time))
    print()

  p4.disconnect()
except P4Exception:
  for e in p4.errors:
      print(e)
