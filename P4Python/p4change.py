from P4 import P4,P4Exception
import re
import config

p4 = P4()
p4.port = config.P4PORT
p4.user = config.P4USER
p4.client = config.P4CLIENT

try:
  p4.connect()

  # Get change specification as text format (p4 change -o)
  textform = p4.fetch_change(tagged=False)
  print(textform)

  # Get change specification as dictionary format (p4 -G change -o)
  dictform = p4.fetch_change()
  print(dictform)
  print(dictform['Description'])

  # Convert text format to dictionary format
  dict_from_text = p4.parse_change( textform )
  print(dict_from_text)
  print(dict_from_text['Description'])

  # Convert text format to dictionary format
  text_from_dict = p4.format_change( dictform )
  print(text_from_dict)

  # Create a new change with the name 'example_client'
  dict_from_text['Description'] = 'example_changelist'
  result = p4.save_change(dict_from_text)

  # Extract change ID from the result
  regex_pattern = re.compile("Change ([1-9][0-9]*) created.")
  match = regex_pattern.match(result[0])
  changeId = '0'
  if match: changeId = match.group(1)
  print(changeId)

  # Delete the change 'example_changelist'
  p4.delete_change(changeId)

  p4.disconnect()
except P4Exception:
  for e in p4.errors:
      print(e)
