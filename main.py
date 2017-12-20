#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import os.path
import sys

def main():
  argv = sys.argv
  argc = len(argv)
  next = os.getcwd()
  if (argc > 1):
      next = argv[1]
  explorer(next)

def explorer(next):
    print(next)
    makeIndex(next)
    list = filter(lambda x: x not in ["directory_index.py", "index.html", ".DS_Store", ".git"], os.listdir(next))
    for x in list:
      p = os.path.abspath(next + '/' + x)
      if os.path.isdir(p):
          explorer(p)

def makeLink(dir, space):
    body = ''
    list = filter(lambda x: x not in ["directory_index.py", "index.html", ".DS_Store", ".git"], os.listdir(dir))
    for x in list:
        p = os.path.abspath(dir + '/' + x)
        for y in range(0, space):
            body += ' '
        if os.path.isdir(p):
          body += '<a href="' + x + '/index.html">' + x + '/</a>\n'
        else:
          body += '<a href="' + x + '">' + x + '</a>\n'
    return body

def makeIndex(dir):
    p = os.path.abspath(dir)
    file = open(p + '/index.html', 'w')
    file.write('<html>\n <body>\n  <h1>Index of /</h1>\n  <hr>\n  <pre>\n' + makeLink(dir, 2) + '  </pre>\n </body>\n</html>')
    file.close()

if __name__ == '__main__':
  main()
