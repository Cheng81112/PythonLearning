'''
操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，
解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。S
AX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
'''

'''
当SAX解析器读到一个节点时会产生3个事件：

start_element事件，在读取<a href="/">时；

char_data事件，在读取python时；

end_element事件，在读取</a>时。
'''


from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)