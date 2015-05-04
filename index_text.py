# coding: utf-8
"""
    index_text.py explores simple Lucene index functionality
    using the gutenberg corpus that comes with NLTK package
"""
# In[3]:

import lucene
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field
from org.apache.lucene.index import IndexWriter, IndexWriterConfig
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.util import Version
import sys 
from java.io import File
import re

lucene.initVM()
index_dir = SimpleFSDirectory(File("index/"))
writerConfig = IndexWriterConfig(Version.LUCENE_4_10_1, StandardAnalyzer())
writer = IndexWriter(index_dir, writerConfig)


# In[56]:

pattern = r"\[([A-Za-z0-9_].*)\]"


# In[26]:

f = open('gutenberg/austen-emma.txt')


# In[76]:

title = f.readline()


# In[77]:

title = re.search(pattern,title.strip()).group(1)


# In[78]:

texts = f.read()


# In[79]:

len(texts)


# In[80]:

doc = Document()
doc.add(Field("title", title, Field.Store.YES, Field.Index.ANALYZED))


# In[81]:

doc.add(Field('text', texts, Field.Store.NO, Field.Index.ANALYZED))


# In[82]:

writer.addDocument(doc)


# In[83]:

f.close()


# In[75]:

f = open('gutenberg/austen-sense.txt')


# In[84]:

writer.close()


# In[86]:

index_dir.close()
