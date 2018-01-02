"""test pickle"""
import re

try:
    import cPickle as pickle  # PY2
except ImportError:
    import pickle

a = b"\x80\x04\x95\x7f\x01\x00\x00\x00\x00\x00\x00}\x94(\x8c\x03url\x94\x8c:http://www.meishij.net/list.php?sortby=update&yl=37&gy=134\x94\x8c\bcallback\x94\x8c\x14_response_downloaded\x94\x8c\aerrback\x94N\x8c\x06method\x94\x8c\x03GET\x94\x8c\aheaders\x94}\x94C\aReferer\x94]\x94C3http://www.meishij.net/list.php?sortby=update&yl=37\x94as\x8c\x04body\x94C\x00\x94\x8c\acookies\x94}\x94\x8c\x04meta\x94}\x94(\x8c\x04rule\x94K\x00\x8c\tlink_text\x94\x8c\nlxml.etree\x94\x8c\x15_ElementUnicodeResult\x94\x93\x94\x8c\x03\xe8\x85\x8c\x94\x85\x94\x81\x94\x8c\x05depth\x94K\x19u\x8c\t_encoding\x94\x8c\x05utf-8\x94\x8c\bpriority\x94K\x00\x8c\x0bdont_filter\x94\x89\x8c\x05flags\x94]\x94u."
b = pickle.loads(a)
print(b)

c = 'http://www.meishij.net/chufang/diy/jiangchangcaipu/157248.html'
h = 'http://www.meishij.net/zuofa/jinqiangyushucaishalaqiubishalazhi.html'

d = re.search(r'/zuofa/\w+\.html$', h)
print(d)

