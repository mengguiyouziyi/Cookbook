"""test pickle"""
import re

try:
    import cPickle as pickle  # PY2
except ImportError:
    import pickle

a = 'http://www.meishij.net/yaoshanshiliao/renqunshanshi/fushe/138397.html'
b = pickle.dumps(a)
print(b)

# c = 'http://www.meishij.net/chufang/diy/jiangchangcaipu/157248.html'
# h = 'http://www.meishij.net/zuofa/jinqiangyushucaishalaqiubishalazhi.html'
#
# d = re.search(r'/zuofa/\w+\.html$', h)
# print(d)

