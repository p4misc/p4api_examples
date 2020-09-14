from P4 import P4,P4Exception
p4 = P4()
p4.port = "1666"
p4.user = "bruno"

try:
  p4.connect()
  # p4 groups
  groups = p4.run( "groups" )
  for group in groups:
    for key in group:
      print(key, "=", group[key])
    print()
  p4.disconnect()
except P4Exception:
  for e in p4.errors:
      print(e)
