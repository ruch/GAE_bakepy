#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import os
import random
import string 

def randcolr():
        return("#" + "".join(random.sample("0123456789abcdef",6)))

def wp(outself,outstr,brk=True):
        outself.response.out.write(outstr)
        if brk==True:
            outself.response.out.write("<br>")
        return

class BakeHandler(webapp.RequestHandler):

  def get(self):
      t = """
      <html>
      <head>
      </head>
      <body>
        ##body##
      </body>
      </html>
      """
      v = self.request.get("signz","virgo")
      n = self.request.get("nbr","42")
      content = ""
      content = content + "your sign is %s <br> \n"%(v)

      n=int(n)
      #<div style="background-color:COLOR">LINE</div>
      for i in range (1 , 11): 
          content = content + "<div style='background-color:%s'> %s x %s = %s </div> \n " %(randcolr(),n,i,n*i)

      op = t.replace("##body##",content)
      self.response.out.write(op)
      return

class stumble (webapp.RequestHandler):

    def get(self):
      t = """
      <html>
      <head>
      <style>
        #p1
        {
            background-color:green;
            padding:1em;
            margin:1em;
            width:8em;
        }
        #p1 a 
        {
            color:white;
        }
      </style>
      </head>
      <body>
        ##body##
      </body>
      </html>
      """
      content = "<div id='p1'><a href='/stumble' id='b1'>Show New Page</a></div>"
      wlist=["http://google.com",
             "http://yahoo.com",
             "http://reddit.com",
             "http://bing.com",
             "http://digg.com",
             "http://kirubakaran.com"] 
      n=random.randint(0,len(wlist)-1)
      content = content + wlist[n] + "<br><iframe src='%s' width='100%%' height='70%%'></iframe>" %(wlist[n])
      #content = content + "<iframe src='%s' width='100%%' height='94%%'></iframe>" %(wlist[n])
      #content = content + "<iframe src='%s' width='800px' height='300'></iframe>" %(wlist[n])
      #content = content + "<iframe src='%s' ></iframe>" %(wlist[n])
      op = t.replace("##body##",content)

      self.response.out.write(op)
      return

def chknum(self,gwrd):
    chknumflg=0
    for i in gwrd:
        if '0123456789'.find(i) >=0 :
            wp(self,'Numbers not allowed <p>')
            chknumflg=1
            break
    return chknumflg

def chkdup(self,gwrd):
    chkdupflg=0
    for i in gwrd:
        if gwrd.count(i) > 1:
            wp(self,'Repeat characters not allowed <p>')
            chkdupflg=1
            break
    return chkdupflg
            
def printresult(self):
    wp(self,'Your Guesses') 
    for i in range(0,len(guesslist)):
        wp(self,guesslist[i],False)
        wp(self,' :- Cows  : ',False)
        wp(self,str(cowscore[i]),False)
        wp(self,'  Bulls : ',False)
        wp(self,str(bullscore[i]))
    return


def comparefunc(self,cwrd,gwrd):
    cow=0
    bull=0
    for i in range(0,4):
        for j in range(0,4):
            if cwrd[i]==gwrd[j]:
                if i==j:
                    bull=bull+1
                else:
                    cow=cow+1
    cowscore.append(cow)
    bullscore.append(bull)
    return bull

def clrall():
    global guesslist
    global theword
    global cowscore
    global bullscore
    global usrguess 
    guesslist=[]
    bullscore=[]
    cowscore=[]
    theword=''
    usrguess=''
    return

guesslist=[]
theword=''
usrguess=''
cowscore=[]
bullscore=[]
class cowbull(webapp.RequestHandler):

  def get(self):
      global guesslist
      global theword
      global usrguess 
      global cowscore
      global bullscore

      t="""<html>
      <head>
      <body>
        <span>
            <p>
            Enter your guess
            </p>
        </span>
        <form name="cbinform" action="cowbull" method="get">
        <input type="text" name="guess" size=4/>
        <input type="submit" value="Submit" size=4/>
        <input type="hidden" name="lose" id="field1"  />
        <input type="submit" value="I Give up" onClick="document.getElementById('field1').value='0'"/>
        </form>
      </body>
      </head>
      </html>
      """

      wordlist=[ 'into',
      'time',
      'more',
      'than',
      'find',
      'long',
      'down',
      'come',
      'made',
      'part',
      'over',
      'take',
      'only',
      'work',
      'know',
      'year',
      'live',
      'back',
      'give',
      'most',
      'very',
      'just',
      'name',
      'help',
      'much',
      'line',
      'mean',
      'same',
      'came',
      'want',
      'show',
      'also',
      'farm',
      'with',
      'they',
      'this',
      'have',
      'from',
      'word',
      'what',
      'when',
      'your',
      'said',
      'each',
      'many',
      'then',
      'them',
      'some',
      'make',
      'like',
      'does',
      'must']

      usrguess= self.request.get("guess").lower()
      loseflg = self.request.get("lose").lower()
      if loseflg =='0':
            wp(self,'Sorry! You lost to : ',False)
            wp(self,theword)
            printresult(self)
            loseflg=''
            clrall()
      if usrguess:
          usrguess = usrguess[0:4]
          if len(usrguess.strip()) < 4:
                  wp(self,'Word too short')
          else:
                chknumflg=chknum(self,usrguess)
                if chknumflg == 0:
                    chkdupflg=chkdup(self,usrguess)
                    if chkdupflg == 0:
                        if len(guesslist) ==0:
                            theword=wordlist[random.randint(0,len(wordlist)-1)]
                        #    wp(self,'theword:')
                            #wp(self,theword)
                        guesslist.append(usrguess)

                        bull=comparefunc(self,theword,usrguess)
                        printresult(self)
                        if bull > 3:
                            wp(self,'********* Congratulations! You win.')
                            clrall()

      self.response.out.write(t)




class readfilez(webapp.RequestHandler):
  def get(self):
      inpath = os.path.join(os.path.dirname(__file__), 'inputz.txt')
      fi=open(inpath,'r')
      rec=fi.read()
      wp(self,rec)
      wp(self,inpath)
      wp(self,os.getcwd())
      wp(self,(os.path.dirname))

def print_tbl(outself,outn):
    t1="""
    <html>
        <head>
        </head>
        <body>
            ##body##
        </body>
    </html>
    """
    content="Multiplication Table <br> <table border=1 style='border-collapse:collapse' cellpadding=10px>"
    for i in range (1 , 11):
        content= content + """
                <tr>
                <td>%s</td>
                <td>x</td>
                <td>%s</td>
                <td>=</td>
                <td>%s</td>
                </tr>
                """ %(outn,i,outn*i)
    content=content + "</table>"
    op=t1.replace("##body##",content)
    wp(outself,op)
    return
class MultHandler(webapp.RequestHandler):
  def get(self):
    t="""
    <html>
        <head>
        </head>
        <body>
            <p>
            Enter a number to see it's multiplication table
            </p>
            <form name="fmmult" action="/mult" method="get">
            <input type="text" name="nbr"/>
            <input type="submit" value="Submit" />
            </form>
        </body>
    </html>
    """
    n=self.request.get("nbr")
    if n:
        n=int(n)
        wp(self,t)
        print_tbl(self,n)
        n=""
    else:
        wp(self,t)

class MainHandler(webapp.RequestHandler):

  def get(self):
    wp(self,"<a href='/stumble'>My Stumble</a>")
    wp(self,"<a href='/bake'>Striped Multiplication Table</a>")
    wp(self,"<a href='/readfilez'>My File Data</a>")
    wp(self,"<a href='/cowbull'>Play CowBull</a>")
    wp(self,"<a href='/mult'>Print Multiplication Table</a>")

def main():
  application = webapp.WSGIApplication([('/', MainHandler),
                                        ('/bake',BakeHandler),
                                        ('/readfilez',readfilez),
                                        ('/cowbull',cowbull),
                                        ('/mult',MultHandler),
                                        ('/stumble',stumble)],
                                       debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
