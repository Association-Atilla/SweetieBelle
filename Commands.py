#-*- coding: utf-8 -*-
#!/usr/bin/env python

''' Kicks a list of users '''
def kick(bot, params):
	bot.say(bot.channels, "As you wish...")
	victims = params.split()
	print bot.channels

	for victim in victims:
		bot.kick(bot.channels, victim,
                         "This conversation can serve no purpose anymore."
                )

def say_moo(bot, params):
	bot.say(bot.channels, "Moooooo!")

def karmic_change(bot, params):
        victim, change = params.split()
        bot.say(bot.channels, victim + " karma has been changed " + change)
