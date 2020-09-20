from P4 import P4,P4Exception
import config

p4 = P4()
p4.port = config.P4PORT
p4.user = config.P4USER

try:
  p4.connect()
  # p4 servers
  servers = p4.run( "servers" )
  for server in servers:
    for key in server:
      print(key, "=", server[key])
    print()
  p4.disconnect()
except P4Exception:
  for e in p4.errors:
      print(e)
