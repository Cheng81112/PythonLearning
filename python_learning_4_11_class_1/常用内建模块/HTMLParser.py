'''
解析HTML文件
利用HTMLPoser，可以把网页中的文本、图像等解析出来

HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，
所以不能用标准的DOM或SAX来解析HTML。
HTMLParser非常方便地解析HTML
'''
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

# 特殊字符有两种，一种是英文表示的&nbsp;
# 一种是数字表示的&#1234;
# 这两种字符都可以通过Parser解析出来。

