#!/usr/bin/python

# Copyright 2013 Joe Walnes and the websocketd team.
# All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import os
from sys import stdout

# Standard CGI(ish) environment variables, as defined in
# http://tools.ietf.org/html/rfc3875
var_names = [
  'AUTH_TYPE',
  'CONTENT_LENGTH',
  'CONTENT_TYPE',
  'GATEWAY_INTERFACE',
  'PATH_INFO',
  'PATH_TRANSLATED',
  'QUERY_STRING',
  'REMOTE_ADDR',
  'REMOTE_HOST',
  'REMOTE_IDENT',
  'REMOTE_PORT',
  'REMOTE_USER',
  'REQUEST_METHOD',
  'REQUEST_URI',
  'SCRIPT_NAME',
  'SERVER_NAME',
  'SERVER_PORT',
  'SERVER_PROTOCOL',
  'SERVER_SOFTWARE',
  'UNIQUE_ID',
  'HTTPS'
]
for var_name in var_names:
  print('%s=%s' % (var_name, os.environ.get(var_name, '<unset>')))
  stdout.flush() # Remember to flush

# Additional HTTP headers
for var_name in os.environ:
  if var_name.startswith('HTTP_'):
    print('%s=%s' % (var_name, os.environ[var_name]))
    stdout.flush() # Remember to flush
