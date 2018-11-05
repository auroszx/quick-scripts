#!/usr/bin/env python2

import asana

client = asana.Client.access_token('your_token_here')	# Get this Asana Connect Token for your account

me = client.users.me()
print "Hello, " + me['name'] 
print "Here are your tasks: \n"

for task in client.tasks.find_all({'workspace': 381426945218034, 'assignee': me['id']}, fields='name,notes,completed'):
	if (not task['completed']):
	  	print ">>>>> "+task['name'] + " <<<<<"
	  	if (task['notes']):
			print "========================================"
		  	print	task['notes']
		  	print "========================================"
	  	for story in client.tasks.stories(task['id']):
	  		if (story['resource_subtype'] == 'comment_added'):
	  			print '\t"'+story['text']+'" - '+story['created_by']['name']
	  	print " "