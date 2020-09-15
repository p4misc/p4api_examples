from P4 import P4,P4Exception
import config

p4 = P4()
p4.port = config.P4PORT
p4.user = config.P4USER

try:
  p4.connect()

  # Get workspace specification as text format (p4 workspace -o)
  textform = p4.fetch_workspace(tagged=False)
  print(textform)

  # Get workspace specification as dictionary format (p4 -G workspace -o)
  dictform = p4.fetch_workspace()
  print(dictform)
  print(dictform['View'])

  # Convert text format to dictionary format
  dict_from_text = p4.parse_workspace( textform )
  print(dict_from_text)
  print(dict_from_text['View'])

  # Convert text format to dictionary format
  text_from_dict = p4.format_workspace( dictform )
  print(text_from_dict)

  # Create a new workspace with the name 'example_client'
  dict_from_text['Client'] = 'example_client'
  dict_from_text['View'] = [ item.replace('none', dict_from_text['Client']) for item in dict_from_text['View'] ]
  p4.save_workspace(dict_from_text)
  print(p4.format_workspace(dict_from_text))

  # Delete the workspace 'example_client'
  p4.delete_workspace(dict_from_text['Client'])

  p4.disconnect()
except P4Exception:
  for e in p4.errors:
      print(e)
