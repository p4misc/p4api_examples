from P4 import P4,P4Exception
p4 = P4()
p4.port = "1666"
p4.user = "bruno"

try:
  p4.connect()
  for status in ["pending", "shelved", "submitted"]:
    # p4 changes -m 10 -u bruno -s status
    changes = p4.run( "changes", "-m", "10", "-u", p4.user, "-s", status )
    for change in changes:
      for key in change:
        print(key, "=", change[key])
      print()
  p4.disconnect()
except P4Exception:
  for e in p4.errors:
      print(e)
