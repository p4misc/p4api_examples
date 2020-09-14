from P4 import P4,P4Exception
import config

p4 = P4()
p4.port = config.P4PORT
p4.user = config.P4USER

try:
  p4.connect()
  # p4 workspaces
  workspaces = p4.run( "workspaces" )
  for workspace in workspaces:
    for key in workspace:
      print(key, "=", workspace[key])
    print()
  p4.disconnect()
except P4Exception:
  for e in p4.errors:
      print(e)
