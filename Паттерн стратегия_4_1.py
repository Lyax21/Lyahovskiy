#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Реализация паттерна стратегия
#Декодирование файлов

class LanguageDecoder(object):
    @staticmethod
    def decode(filename):
        raise NotImplementedError()

#Стратегии 
class HtmlDecoder(LanguageDecoder):
    @staticmethod
    def decode(filename):
        print('HTML decode')
 
 
class PhpDecoder(LanguageDecoder):
    @staticmethod
    def decode(filename):
        print ('PHP decode')
 
 
class CDecoder(LanguageDecoder):
    @staticmethod
    def decode(filename):
        print ('C decode')


class CppDecoder(LanguageDecoder):
    @staticmethod
    def decode(filename):
        print('C++ decode')
 
 
class JsDecoder(LanguageDecoder):
    @staticmethod
    def decode(filename):
        print ('JavaScript decode')
 
 
class PythonDecoder(LanguageDecoder):
    @staticmethod
    def decode(filename):
        print ('Python decode')


class File(object):
    @classmethod
    def open(cls, filename):
        ext = filename.rsplit('.', 1)[-1]
        if ext == 'html':
            decoder = HtmlDecoder
        elif ext in ('php'):
            decoder = PhpDecoder
        elif ext == 'c':
            decoder = CDecoder
        elif ext in ('cpp', 'cxx'):
            decoder = CppDecoder
        elif ext == 'js':
            decoder = JsDecoder
        elif ext == 'py':
            decoder = PythonDecoder
        else:
            raise RuntimeError('Невозможно декодировать файл %s' % filename)
        byterange = decoder.decode(filename)
        return cls(byterange, filename)
 
    def __init__(self, byterange, filename):
        self._byterange = byterange
        self._filename = filename
 
 
File.open('file.html')  # html decode
File.open('file.php')  # php decode
File.open('file.c')  # c decode
File.open('file.cpp')  # cpp decode
File.open('file.js')  # js decode
File.open('file.py')  # py decode


# In[ ]:




