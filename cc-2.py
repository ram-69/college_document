from google.appengine.ext import webapp
from google.appengine.ext.webapp import util


class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('<h1>Hello world suagdvuiaFWF!</h1>')
        self.response.out.write("<br />")
        self.response.out.write('<img src="https://www.w3schools.com/tags/img_girl.jpg" alt="Girl in a jacket" width="500" height="600">                          ')
        self.response.out.write("<br />")
        self.response.out.write('#####################')


def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
