from P4 import P4,P4Exception
import config

p4 = P4()
p4.port = config.P4PORT
p4.user = config.P4USER

try:
  p4.connect()

  # Get user specification as dictionary format (p4 -G user -o)
  dictform = p4.fetch_user('example_user')
  print(dictform)

  # Create a new user with the name 'example_user'
  dictform['Email'] = 'example_user@localhost.com'
  dictform['FullName'] = 'Example User'
  p4.save_user(dictform, '-f')
  print(dictform)

  # Delete the user 'example_client'
  p4.delete_user('-f', dictform['User'])

  p4.disconnect()
except P4Exception:
  for e in p4.errors:
      print(e)
