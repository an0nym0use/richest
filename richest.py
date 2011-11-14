# packages
import os
import cgi
import urllib2
import re
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
	def get(self):
		richest_page = urllib2.urlopen(urllib2.Request("http://richestontheweb.com")).read()
		richest_so_far = re.search('became the #RichestOnTheWeb by paying \$[0-9.]{2,8}',richest_page).group(0)[39:-1]
		amount = float(sum(xrange(1,int(float(richest_so_far)*100)+1)))/100
		template_values = {
			'amount': amount
		}
		path = os.path.join(os.path.dirname(__file__), 'index.html')
		self.response.out.write(template.render(path, template_values))

app = webapp.WSGIApplication([('/',MainPage)],debug=True)

def main():
	run_wsgi_app(app)

if __name__ == "__main__":
	main()
