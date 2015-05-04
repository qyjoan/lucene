
# coding: utf-8

# In[15]:

import lucene
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import IndexReader
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.util import Version
import sys 
from java.io import File


# In[21]:

lucene.initVM()
analyzer = StandardAnalyzer(Version.LUCENE_4_10_1)
index_dir = SimpleFSDirectory(File("index/"))


# In[22]:

reader = IndexReader.open(index_dir)
n_docs = reader.numDocs()
print("Index contains %d documents." % n_docs)


# In[23]:

query = QueryParser(Version.LUCENE_4_10_1, "text", analyzer).parse("Knightley")


# In[26]:

searcher = IndexSearcher(reader)
hits = searcher.search(query, 10)


# In[27]:

hits


# In[34]:

print hits.totalHits
for hit in hits.scoreDocs:
    print hit.score, hit.doc, hit.toString()
    doc = searcher.doc(hit.doc)
    print doc.get("title").encode("utf-8")


