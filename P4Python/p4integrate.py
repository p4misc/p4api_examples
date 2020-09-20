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

  dummy_file1 = pathlib.Path(workspace._Root + '\\dummy_file1.txt')
  dummy_file2 = pathlib.Path(workspace._Root + '\\dummy_file2.txt')
  # Delete the file if it is in the local directory
  for dummy_file in [dummy_file1, dummy_file2]:
    if dummy_file.exists():
      dummy_file.chmod(stat.S_IWUSR)
      dummy_file.unlink()

    # p4 obliterate -y the file if it is in the depot
    if p4.run_files(str(dummy_file)):
      p4.run_obliterate('-y', str(dummy_file))

  dummy_file1.write_text('add dummy file')
 
  # p4 add
  p4.run_add(str(dummy_file1))
  default_change = p4.fetch_change()
  default_change._description = 'add a new file'
  print(default_change)
 
  # p4 submit
  submitted_change = p4.run_submit(default_change)
  print(submitted_change)
 
  # p4 populate
  submitted_change = p4.run_populate('-d', 'branch an existing file', str(dummy_file1), str(dummy_file2))
  print(submitted_change)

  # p4 edit
  p4.run_edit(str(dummy_file1))
  dummy_file1.write_text('edit dummy file')
  default_change = p4.fetch_change()
  default_change._description = 'edit the dummy_file1'
  print(default_change)

  # p4 submit
  submitted_change = p4.run_submit(default_change)
  print(submitted_change)
 
  # p4 integrate
  p4.run_integrate(str(dummy_file1), str(dummy_file2))
  default_change = p4.fetch_change()
  default_change._description = 'integrate the dummy_file1 into the dummy_file2'
  print(default_change)

  # p4 resolve
  p4.run_resolve('-as', '-Ac', str(dummy_file2))
  default_change = p4.fetch_change()
  default_change._description = 'integrate the dummy_file1 into the dummy_file2'
  print(default_change)

  # p4 submit
  submitted_change = p4.run_submit(default_change)
  print(submitted_change)

  p4.disconnect()
except P4Exception:
  for e in p4.errors:
      print(e)
