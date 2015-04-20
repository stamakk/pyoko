# -*-  coding: utf-8 -*-
"""
riak client configuration
"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.

import riak
from riak.security import SecurityCreds
from local_settings import SERVER_IP


creds = SecurityCreds(username='esat', password='qwe-asd', cacert_file='riak.crt')
# client = riak.RiakClient(protocol='pbc', host=SERVER_IP, pb_port='8087', credentials=creds)

pbc_client = riak.RiakClient(protocol='pbc', host=SERVER_IP, pb_port='8087')
http_client = riak.RiakClient(protocol='http', host=SERVER_IP, http_port='8098')

z1_pbc_client = riak.RiakClient(protocol='pbc', host='z1.zetaops.io', pb_port='18087')
z1_http_client = riak.RiakClient(protocol='http', host='z1.zetaops.io', http_port='18098')

