import webapp2
import jinja2
import os
import logging

from google.appengine.api import users
from google.appengine.ext import ndb

#class Message(ndb.Model):
    #message_content = ndb.StringProperty()

class User(ndb.Model):
    email = ndb.StringProperty()

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


class Settings(ndb.Model):
    # The amount of reminders set.
    reminder_frequency_setting = ndb.StringProperty()
    # The type of reminders set.
    reminder_type_setting = ndb.StringProperty()
    # The amount of snoozes allowed.
    reminder_snooze_setting = ndb.IntegerProperty()
    # The user associated with a set of settings.
    setting_user_id = ndb.StringProperty()

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #User email
        email = str(users.get_current_user().email())
        # Gets all of the timers in the database.
        timers = Timer.query().fetch()
        # Gets the current user ID.
        # user_id = self.request.get('user')
        logging.info(help(users.get_current_user()))
        user_id = users.get_current_user().user_id()
        # User logout
        logout_url = users.create_logout_url('/login')

        template_values = {'timers':timers, 'user_id':user_id, 'logout': logout_url, 'email': email}
        template = jinja_environment.get_template('main.html')
        self.response.write(template.render(template_values))

    def post(self):
        user_id = users.get_current_user().user_id()
        task = str(self.request.get('task'))
        break_length = int(self.request.get('break_length'))
        reminder_amount = int(self.request.get('reminder_amount'))
        reminder_frequency = int(self.request.get('reminder_frequency'))

        new_timer = Timer(timer_task=task, break_length=break_length, reminder_amount=reminder_amount, reminder_frequency=reminder_frequency, user_id=user_id)
        new_timer.put()

        self.redirect('/timer?user=' + user_id + '&key=' + new_timer.key.urlsafe())

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            self.redirect('/')

        else:
            login_url = users.create_login_url('/')


        template = jinja_environment.get_template('log_in.html')
        template_values = {'login': login_url}
        self.response.write(template.render(template_values))


class SettingsHandler(webapp2.RequestHandler):
    def get(self):
        user_id = str(self.request.get('user'))
        existing_settings = Settings.query(Settings.setting_user_id == user_id).fetch()

        template_values = {"settings":existing_settings}

        template = jinja_environment.get_template('settings.html')
        self.response.write(template.render())

    def post(self):
        user_id = str(self.request.get('user'))
        reminder_amount = str(self.request.get('reminder'))
        message_type = str(self.request.get('message_type'))
        snoozes_allowed = int(self.request.get('snoozes'))

        existing_settings = Settings.query(Settings.setting_user_id == user_id).fetch()
        existing_settings = Settings(reminder_frequency_setting=reminder_amount, reminder_type_setting=message_type, reminder_snooze_setting=snoozes_allowed, setting_user_id=user_id)
        existing_settings.put()

        self.redirect('/settings?user=' + user_id)

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
        user_ID = str(self.request.get('user'))
        timers = Timer.query(Timer.user_id == user_ID).fetch()

        template = jinja_environment.get_template('user_log.html')
        template_values = {'timers': timers}
        self.response.write(template.render(template_values))

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
