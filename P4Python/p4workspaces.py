from P4 import P4,P4Exception
p4 = P4()
p4.port = "1666"
p4.user = "bruno"

try:
  p4.connect()
  workspaces = p4.run( "workspaces" )
  for workspace in workspaces:
    for key in workspace:
      print(key, "=", workspace[key])
    print()
  p4.disconnect()
except P4Exception:
  for e in p4.errors:
      print(e)
