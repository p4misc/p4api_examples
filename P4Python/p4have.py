from P4 import P4,P4Exception
import os
import re
import inspect
import config

p4 = P4()
p4.port = config.P4PORT
p4.user = config.P4USER
p4.client = config.P4CLIENT

try:
  p4.connect()

  # p4 workspace -o 
  files = p4.run_have("//...")

  for file in files:
    print("Revision #%s %s %s %s %s" % (file['haveRev'],file['depotFile'],file['clientFile'],file['path'],file['syncTime']))

  p4.disconnect()
except P4Exception:
  for e in p4.errors:
      print(e)
