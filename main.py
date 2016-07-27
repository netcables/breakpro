import webapp2
import jinja2
import os

from google.appengine.api import users
from google.appengine.ext import ndb

#class Message(ndb.Model):
    #message_content = ndb.StringProperty()

class ModelWithUser(ndb.Model):
    user_id = ndb.StringProperty()

class Timer(ndb.Model):
    # The task listed with a timer.
    timer_task = ndb.StringProperty()
    # The length of a break.
    break_length = ndb.IntegerProperty()
    # The amount of reminders requested after time is up.
    reminder_amount = ndb.IntegerProperty()
    # The amount of time between reminders.
    reminder_frequency = ndb.IntegerProperty()
    # The user id associated with a timer.
    user_id = ndb.StringProperty()

class Reminder(ndb.Model):
    # The message associated with a reminder.
    message = ndb.StringProperty()
    # The task associated with a reminder.
    task = ndb.StringProperty()
    # The timer key associated with a reminder.
    timer_key = ndb.KeyProperty(kind=Timer)

class Settings(ndb.Model):
    # The amount of reminders set.
    reminder_frequency_setting = ndb.StringProperty()
    # The type of reminders set.
    reminder_type_setting = ndb.StringProperty()
    # The amount of snoozes allowed.
    reminder_snooze_setting = ndb.StringProperty()
    # The user associated with a set of settings.
    setting_user_id = ndb.StringProperty()

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # Gets all of the timers in the database.
        timers = Timer.query().fetch()
        # Gets all of the reminders in the database.
        reminders = Reminder.query().fetch()
        # Gets the current user ID.
        user_id = self.request.get('user')

        template_values = {'timers':timers, 'reminders':reminders, 'user_id':user_id}
        template = jinja_environment.get_template('main.html')
        self.response.write(template.render(template_values))

    def post(self):
        user_id = str(self.request.get('user'))
        task = str(self.request.get('task'))
        break_length = int(self.request.get('break_length'))
        reminder_amount = int(self.request.get('reminder_amount'))
        reminder_frequency = int(self.request.get('reminder_frequency'))

        new_timer = Timer(timer_task=task, break_length=break_length, reminder_amount=reminder_amount, reminder_frequency=reminder_frequency, user_id=user_id)
        new_timer.put()

        self.redirect('/timer?user=' + user_id + '&key=' + new_timer.key.urlsafe())

    def settings_switch(self):
        user_id = str(self.request.get('user'))
        self.redirect('/settings?user=' + user_id)


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            template = jinja_environment.get_template('main.html')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(nickname, logout_url)
            user_id = user.user_id()
            template_values = {'user_id':user_id}
            self.redirect('/?user=' + user_id)
            # self.response.write(template.render(template_values))

        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)

        self.response.write(
            '<html><body>{}</body></html>'.format(greeting))
        template = jinja_environment.get_template('log_in.html')
        #template_values?
        self.response.write(template.render())


class SettingsHandler(webapp2.RequestHandler):
    def get(self):
        user_id = str(self.request.get('user'))
        existing_settings = Settings.query(Settings.setting_user_id == user_id).fetch()

        template = jinja_environment.get_template('settings.html')
        #template_values?
        self.response.write(template.render())

    def post(self):
        user_id = str(self.request.get('user'))
        message_type = str(self.request.get('message_type'))
        snoozes_allowed = int(self.request.get('snoozes'))

class TimerHandler(webapp2.RequestHandler):
    def get(self):
        urlsafe_key = self.request.get('key')

        timer_key = ndb.Key(urlsafe=urlsafe_key)
        timer = timer_key.get()

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
        #template_value
        self.response.write(template.render())

class FriendHandler(webapp2.RequestHandler):
    def get(self):

        template = jinja_environment.get_template('friends.html')
        #template_values?
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LoginHandler),
    ('/settings', SettingsHandler),
    ('/timer',TimerHandler),
    ('/user_log', UserLogHandler),
    ('/alert', AlertHandler),
    ('/friends', FriendHandler)
], debug=True)
