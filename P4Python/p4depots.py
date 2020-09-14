from P4 import P4,P4Exception
p4 = P4()
p4.port = "1666"
p4.user = "bruno"

try:
  p4.connect()
  depots = p4.run( "depots" )
  for depot in depots:
    for key in depot:
      print(key, "=", depot[key])
    print()
  p4.disconnect()
except P4Exception:
  for e in p4.errors:
      print(e)
