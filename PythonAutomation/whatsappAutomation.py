import pywhatkit

#Sending a message to a contact
pywhatkit.sendwhatmsg('+1xxxxxx', "Test", 4, 22, 15, True, 2)

#Sending a message to an ID
pywhatkit.sendwhatmsg_to_group('id Number', "Test Group", 4, 45, 15, True, 4)