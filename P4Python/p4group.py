from P4 import P4,P4Exception
import config

p4 = P4()
p4.port = config.P4PORT
p4.user = config.P4USER

try:
  p4.connect()

  # Get user specification as dictionary format (p4 -G group -o)
  dictform = p4.fetch_group('example_group')
  print(dictform)

  # Create a new group with the name 'example_user'
  dictform['Timeout'] = 'unlimited'
  dictform['Users'] = [ p4.user ]
  p4.save_group(dictform)
  print(dictform)

  # Delete the group 'example_client'
  p4.delete_group(dictform['Group'])

  p4.disconnect()
except P4Exception:
  for e in p4.errors:
      print(e)
