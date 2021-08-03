# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:27:26 2021

@author: spllul
"""

import sqlalchemy as sal
from sqlalchemy import create_engine
import pandas as pd
from urllib.parse import quote

engine = create_engine('oracle+cx_oracle://sqldemo:%s@XE' % quote('sas94@sas'),echo='debug')
con = engine.connect()
outpt = con.execute("SELECT table_name FROM user_tables ORDER BY table_name")
df = pd.DataFrame(outpt.fetchall())
df.columns = outpt.keys()
print(df.head())

outpt = con.execute("SELECT * FROM DEMO_CUSTOMERS where rownum <= 10")
df = pd.DataFrame(outpt.fetchall())
df.columns = outpt.keys()
print(df.head())

con.close() 