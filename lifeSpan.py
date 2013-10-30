#!/usr/bin/python

#####################################################################
#####################################################################
#############################LIFE_SPAN-##############################
#####################################################################
#####################################################################


#####################################################################
# Variables below are for calculations to do with age.###############
#####################################################################

months_in_a_year = 12
days_in_a_year = 365
weeks_in_a_year = days_in_a_year / 7
hours_in_a_year = days_in_a_year * 24
minutes_in_a_year = hours_in_a_year * 60
seconds_in_a_year = minutes_in_a_year * 60

#####################################################################
# Below is the programme.############################################
#####################################################################

name = raw_input("Hello, first of all, what is your name? ")

print "\n"

print "Why hello there", name

print "\n"

age = input("And how old are you? ")

print "\n"

if age <= 24:
	
	print "Ahhh, so you're %s, still a young whippersnapper then I see!" % age

else:

	print "Getting on a bit I see.."

print "\n"

print "With your permission, I will give you a more in-depth span of your life"

print "\n"

answer = raw_input("So, do you wish to carry on? Answer yes or no.. ")

print "\n"

if answer == "yes":
	
	print "Right then, let's carry on.."
	
	import time
	time.sleep(2)
	
	print "\n"
	
	months_lived = age * months_in_a_year
	weeks_lived = age * weeks_in_a_year
	days_lived = age * days_in_a_year
	hours_lived = age * hours_in_a_year
	minutes_lived = age * minutes_in_a_year
	seconds_lived = age * seconds_in_a_year
	
	print "So then %s, from my calculations, I have worked out that you have lived..\n\n\t*%s months\n\t*%s weeks\n\t*%s days\n\t*%s hours\n\t*%s minutes\n\t*%s seconds" % (name, months_lived, weeks_lived, days_lived, hours_lived, minutes_lived, seconds_lived)
	
	print "\n"
	
	print "Hope this enlightens you in some way %s." % name
	
else:
	
	print "Let's get outta here!!"
