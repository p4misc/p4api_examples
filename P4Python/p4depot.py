from P4 import P4,P4Exception
import config

p4 = P4()
p4.port = config.P4PORT
p4.user = config.P4USER

try:
  p4.connect()

  # Get depot specification as dictionary format (p4 -G depot -o)
  dictform = p4.fetch_depot('example_depot')
  print(dictform)

  # Create a new depot with the name 'example_depot'
  dictform['Type'] = 'stream'

  # Change the stream depth of the depot to 2
  dictform['StreamDepth'] = dictform['StreamDepth'] + '/2'
  p4.save_depot(dictform)
  print(dictform)

  # Delete the depot 'example_client'
  p4.delete_depot(dictform['Depot'])

  p4.disconnect()
except P4Exception:
  for e in p4.errors:
      print(e)
