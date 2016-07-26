import webapp2
import jinja2
import os

from google.appengine.ext import ndb

#class Message(ndb.Model):
    #message_content = ndb.StringProperty()

class Timer(ndb.Model):
    # The task listed with a timer.
    timer_task = ndb.StringProperty()
    # The length of a break.
    break_length = ndb.IntegerProperty()
    # The amount of reminders requested after time is up.
    reminder_amount = ndb.IntegerProperty()
    # The amount of time between reminders.
    reminder_frequency = ndb.IntegerProperty()

class Reminder(ndb.Model):
    # The message associated with a reminder.
    message = ndb.StringProperty()
    # The task associated with a reminder.
    task = ndb.StringProperty()
    # The timer key associated with a reminder.
    timer_key = ndb.KeyProperty(kind=Timer)

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        timers = Timer.query().fetch()
        reminders = Reminder.query().fetch()

        template_values = {'timers':timers, 'reminders':reminders}
        template = jinja_environment.get_template('main.html')
        self.response.write(template.render(template_values))

    def post(self):
        task = str(self.request.get('task'))
        break_length = int(self.request.get('break_length'))
        reminder_amount = int(self.request.get('reminder_amount'))
        reminder_frequency = int(self.request.get('reminder_frequency'))

        new_timer = Timer(timer_task=task, break_length=break_length, reminder_amount=reminder_amount, reminder_frequency=reminder_frequency)
        new_timer.put()

        self.redirect('/timer?key=' + new_timer.key.urlsafe())


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
        urlsafe_key = self.request.get('key')

        key = ndb.Key(urlsafe=urlsafe_key)
        timer = key.get()

        template_values = {"timer":timer}

        template = jinja_environment.get_template('timer.html')
        self.response.write(template.render(template_values))

    def post(self):

        template_values = {"timer":timer}
        template = jinja_environment.get_template('timer.html')
        self.response.write(template_render(template_values))

class UserLogHandler(webapp2.RequestHandler):
    def get(self):

        template = jinja_environment.get_template('user_log.html')
        #template_values?
        self.response.write(template.render())

class AlertHandler(webapp2.RequestHandler):
    def get(self):

        template = jinja_environment.get_template('alert.html')
        #template_values?
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LoginHandler),
    ('/settings', SettingsHandler),
    ('/timer',TimerHandler),
    ('/user_log', UserLogHandler),
    ('/alert', AlertHandler)
], debug=True)
