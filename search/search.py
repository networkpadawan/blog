#!/usr//bin/python
import os
from flask import Flask, render_template
from flask import request, jsonify
from whoosh import index, qparser, highlight
from whoosh.qparser.dateparse import DateParserPlugin
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField
from whoosh.query import Query, And, Or, Term, FuzzyTerm, Not, Regex, TermRange, DateRange, Every
from whoosh.qparser import QueryParser
from whoosh.index import create_in, open_dir
class Search(Form):
    search = TextField("Type to Search")
"add search by title"
ix = open_dir('index')
def wsearch(a):
        qp = QueryParser("body",schema=ix.schema)
        q = qp.parse(a)
        with ix.searcher() as searcher:
                results = searcher.search(q)
                return render_template('search_post.html', results=results)

app = Flask(__name__, template_folder="/root/peliboo/templates")

@app.route('/search', methods=['GET', 'POST'])
def search():
        form = Search(csrf_enabled=False)

        if request.method == 'POST':
                b = form.search.data
                return wsearch(b)

        if request.method == 'GET':
                return render_template('search_get.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
