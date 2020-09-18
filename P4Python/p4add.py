from P4 import P4,P4Exception
import os
import re
import pathlib
import config

p4 = P4()
p4.port = config.P4PORT
p4.user = config.P4USER
p4.client = config.P4CLIENT

try:
  p4.connect()

  # p4 workspace -o 
  workspace = p4.fetch_workspace(p4.client)

  dummy_file = pathlib.Path(workspace._Root + '\\dummy_file.txt')
  with dummy_file.open(mode='w') as file:
    file.write('dummy file')

  # p4 add file
  p4.run_add(str(dummy_file))
  default_change = p4.fetch_change()
  default_change._description = 'add a new file'
  print(default_change)

  # p4 revert file
  p4.run_revert(str(dummy_file))
  default_change = p4.fetch_change()
  print(default_change)

  p4.disconnect()
except P4Exception:
  for e in p4.errors:
      print(e)
