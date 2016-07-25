import webapp2
import jinja2
import os

from google.appengine.ext import ndb

#class Message(ndb.Model):
    #message_content = ndb.StringProperty()

class Reminder(ndb.Model):
    message = ndb.StringProperty()
    task = ndb.StringProperty()


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('main.html')
        #template_values?
        self.response.write(template.render())

class LoginHandler(webapp2.RequestHandler):
    def get(self):

        template = jinja_environment.get_template('log_in.html')
        #template_values?
        self.response.write(template.render())

class SettingsHandler(webapp2.RequestHandler):
    def get(self):

        template = jinja_environment.get_template('settings.html')
        #template_values?
        self.response.write(template.render())

class TimerHandler(webapp2.RequestHandler):
    def get(self):

        template = jinja_environment.get_template('timer.html')
        #template_values?
        self.response.write(template.render())

class UserLogHandler(webapp2.RequestHandler):
    def get(self):

        template = jinja_environment.get_template('user_log.html')
        #template_values?
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LoginHandler),
    ('/settings', SettingsHandler),
    ('/timer',TimerHandler),
    ('/user_log', UserLogHandler)
], debug=True)
