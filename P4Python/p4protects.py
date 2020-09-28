from P4 import P4,P4Exception
import config

p4 = P4()
p4.port = config.P4PORT
p4.user = config.P4USER

try:
  p4.connect()
  # p4 protects -u sample_user
  protects = p4.run( 'protects', '-u', 'sample_user' )
  for protect in protects:
    for key in protect:
      print(key, "=", protect[key])
    print()
  p4.disconnect()
except P4Exception:
  for e in p4.errors:
      print(e)
