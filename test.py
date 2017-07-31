#!/usr/bin/python
# -*- coding: utf8 -*-
from pyvi.pyvi import ViTokenizer, ViPosTagger
import re, itertools
import math,os
import pandas as pd
import json
from cassandra.io.libevreactor import LibevConnection
from cassandra.cluster import Cluster
from cassandra.query import dict_factory
import facebook
import time

cluster = Cluster()
cluster.connection_class = LibevConnection
session = cluster.connect('getfb')
rows = session.execute('SELECT * FROM getdata')

for row in rows:
    print row.comment