from P4 import P4,P4Exception
import os
import re
import stat
import pathlib
import config

p4 = P4()
p4.port = config.P4PORT
p4.user = config.P4USER
p4.client = config.P4CLIENT
p4.exception_level = 1

try:
  p4.connect()

  # p4 workspace -o 
  workspace = p4.fetch_workspace(p4.client)

  dummy_file = pathlib.Path(workspace._Root + '\\dummy_file.txt')
  # Delete the file if it is in the local directory
  if dummy_file.exists():
    dummy_file.chmod(stat.S_IWUSR)
    dummy_file.unlink()

  # p4 obliterate -y the file if it is in the depot
  if p4.run_files(str(dummy_file)):
    p4.run_obliterate('-y', str(dummy_file))

  dummy_file.write_text('add dummy file')

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
