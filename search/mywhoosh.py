import os,codecs,re
import whoosh
from whoosh import index
from whoosh.index import create_in 
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED, DATETIME
from whoosh.analysis import StemmingAnalyzer, KeywordAnalyzer
from whoosh.query import Query, And, Or, Term, FuzzyTerm, Not, Regex, TermRange, DateRange, Every
from whoosh.qparser import QueryParser
from whoosh.writing import AsyncWriter
from whoosh.sorting import ScoreFacet, MultiFacet, FieldFacet 
path = "/root/search/list.txt"
path2 = "/root/blog/"
# Set index
schema = Schema(
            title = ID(stored=True,unique=True),
            body = TEXT(stored=True,analyzer=StemmingAnalyzer()),
            date = DATETIME(stored=True),
            link = TEXT(stored=True),
)

# Create index dir if it does not exists.
dic = {":title: ":"",":Title:":""," Title: ":"","title: ":""}
if not os.path.exists("index"):
    os.mkdir("index")
index = create_in("index", schema)
writer = index.writer()
for title in open(path).read().splitlines():
        file = open(path2 +title, "r")
        lines = file.readlines()
        file.close()
        url_date = lines[2].split()
        url_date =  url_date[1].split("-")
	if title.endswith(".rst"):
	        title = lines[0].replace(':title: ','')
	else:
        	title = lines[0].replace('Title: ','')
        body = "".join(lines[4:-1])
        link = "https://tiagoasousa.pt/"+url_date[0]+"/"+url_date[1]+"/"+title
        writer.add_document(title=unicode(title, "utf-8"), body=unicode(body, "utf-8"),link=unicode(link, "utf-8"))
writer.commit()

