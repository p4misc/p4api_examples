from P4 import P4,P4Exception
import config

p4 = P4()
p4.port = config.P4PORT
p4.user = config.P4USER

try:
  p4.connect()
  # p4 configure show
  configures = p4.run( "configure", "show" )
  for configure in configures:
    print('Type = ' + configure['Type'])
    print('Name = ' + configure['Name'])
    print('Value = ' + configure['Value'])
    print()

  # p4 configure show allservers
  configures = p4.run( "configure", "show", "allservers" )
  for configure in configures:
    print('Type = ' + configure['Type'])
    print('Name = ' + configure['Name'])
    print('Value = ' + configure['Value'])
    print()
  p4.disconnect()
except P4Exception:
  for e in p4.errors:
      print(e)
