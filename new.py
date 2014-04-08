import urllib2
import re
file = open('workfile.txt', 'r')
female=0
male=0
link = file.readline()
while link : 
	f = urllib2.urlopen(link)
	string = f.read()
	fblink = re.search('(facebook.com/profile.php\?id=\d+)',string)
	if fblink:
		fblink = fblink.group(0)
		id = fblink.split('=')
		graphurl = 'https://graph.facebook.com/' + id[1]
		fr = urllib2.urlopen(graphurl)
		graphdata = fr.read()
		gen = re.search('("gender":"\w+")',graphdata) 
		gender = gen.group(0).split(':')[1]
		#print gender
		if gender == '"female"' :
			female = female + 1
		else:	
			male = male + 1
		print "female = " + str(female) + " & Male = " + str(male)
	link = file.readline()
		
