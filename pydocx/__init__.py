from .parsers import Docx2LaTex, Docx2Html, Docx2Markdown
from HtmlConversion import Html2Docx


def docx2html(path):
    return Docx2Html(path).parsed


def docx2markdown(path):
    return Docx2Markdown(path).parsed

<<<<<<< HEAD

def docx2latex(path):
    return Docx2LaTex(path).parsed

def html2docx(path):
    return Html2Docx(path).parsed

VERSION = '0.3.1'
=======
VERSION = '0.3.2'
>>>>>>> c46e8647a29e711476f258eb9629b90513e86991
