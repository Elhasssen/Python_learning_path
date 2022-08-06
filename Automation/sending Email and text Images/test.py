# import ezgmail, os
# ######################################
# os.chdir(r'C:\Users\ElHassen\Desktop\Python\learningpy\sending Email and text Images')
# ezgmail.init()
##########################################
# ezgmail.send('younes011@gmail.com', 'test', 'hey this email is sent by a python script')
# # or you can add an attachement
# # AS : 
# ezgmail.send('blbll@ggg.com', 'haha' , 'hhah haha haah hah', ['ffdsfdsf','fdsfdsf'])
# # or you need to forward the email to someone else 

# ezgmail.send('hahaha@gmail.com', 'hello', 'bal lblae lfdlf lfd', cc='dsdqsdqsd@gmail.com', bcc ='rezrzerjkzerzer@gmail.com, someonelese@gmail.com')
####################################
# # if we need to rememebr the email we are workin with
# # or the token.js is attached to 
# print(ezgmail.EMAIL_ADDRESS)
# # output : hasseneanf16@gmail.com
#######################################
# or reading mail for a gmail account
# unreadthreads = ezgmail.unread()
# print(ezgmail.summary(unreadthreads))
# output : unread emails will be printed 
####################################### 
# # searching email from a gmail Account : 
# resultThread = ezgmail.search('pixelo')
# print(len(resultThread))
# # output : we found out that there is 25 emails that concerns Pixelo
###########################################
# also we can download attachmeent from a gmail account
# threads = ezgmail.search('vacation photos')
# threads[0].messages[0].attachments
# ['tulipe.jpg','canal.jpg','bicycles.jpg']
#############################################
# SMTP, simple mail trasfer protocol
# SMTP deals with sending emails to others
##################################
# sending email :
import smtplib
smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
print(type(smtpobj))
# output : <class 'smtplib.SMTP'>
# the SMTP object dictates that there is a connection to 
# the server
print(smtpobj.ehlo())
# output : <class 'smtplib.SMTP'>
# (250, b'smtp.gmail.com at your service,
# [105.235.137.62]\nSIZE 35882577\n8BITMIME\
# nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING
# \nCHUNKING\nSMTPUTF8')
# Starting TLS encryption
# the reason to do this is to enable encyption for the connection
# if we are using 465 (using SSL) the encyption is already set up 
print(smtpobj.starttls())
# the starttls() puts your SMTP connection in TLS mode 
# the 220 return value tell you the server is ready 
##############################
# loggin in to the SMTP server 
print(smtpobj.login('hasseneanf16@gmail.com', 'hassenebo.milano2006914789'))
# the logging in wo'nt happen because the gamil is considered 
# SMTP as less secure app
# go here to import it : https://myaccount.google.com/lesssecureapps
# output : (235, b'2.7.0 Accepted')
# the 235 code means it is accepted 
################
# Sending Email 
# smtpobj.sendmail('hasseneanf16@gmail.com', 'boumeddiene.elhassen@gmail.com', 'subject : so long.\n Dear hassen, thanks hassen for sticking a long with yourself, sincerly, hassen')
# The start of the email body string must begin with 'Subject: \n' for the subject line of the email. The '\n'
# newline character separates the subject line from the main body of the email.
# disconneting from the SMTP Server 

print(smtpobj.quit())
# output : (221, b'2.0.0 closing connection y4-20020adff144000000b001f022290737sm7281440wro.6 - gsmtp')

# IMAP Client : is the opposite of SMTP , it specifies how to communciate
# with Mail server to retreive emails sent to your email address

#################
# SMS sending not avaialvle for algeria and only in the united states 

####################################
