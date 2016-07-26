import webapp2
import jinja2
import os

from google.appengine.ext import ndb

#class Message(ndb.Model):
    #message_content = ndb.StringProperty()

class Reminder(ndb.Model):
    message = ndb.StringProperty()
    task = ndb.StringProperty()

class Timer(ndb.Model):
    # The task listed with a timer.
    timer_task = ndb.IntegerProperty()
    # The length of a break.
    break_length = ndb.IntegerProperty()
    # The amount of reminders requested after time is up.
    reminder_amount = ndb.IntegerProperty()
    # The amount of time between reminders.
    reminder_frequency = ndb.IntegerProperty()

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('main.html')
        #template_values?
        self.response.write(template.render())

    def post(self):
        task = self.request.get('task')
        break_length = self.request.get('break_length')
        reminder_amount = self.request.get('reminder_amount')
        reminder_frequency = self.request.get('reminder_frequency')

        new_timer = Timer(timer_task=task, break_length=break_length,
        reminder_amount=reminder_amount, reminder_frequency=reminder_frequency)
        new_timer.put()


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

    def post(self):

        template_values = {"timer":timer}
        template = jinja_environment.get_template('timer.html')
        self.response.write(template_render(template_values))

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
