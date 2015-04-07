import sys, time
from colors import red, blue, green, bold, yellow
import random

def help():
	print bold('''*DZERO HELP*
	
Enter the letter [b] to open up the backpack.
Enter the letter [l] to inspect current room again.

To use items in the backpack, enter the name of the item.
To inspect items, doors, etc of a room, type "inspect [element]".\n''')
	raw_input('Press [Enter] to continue... ')
	print '\n'

def backpack():
	global bars
	global bp
	global flash
	global sword
	global potion
	global tri
	global hex
	print "Items in backpack:"
	for items in bp:
		print "   - %s" % bold(items)
	use = raw_input("Choose an item for %s to use(press [c] to close): " % name)
	if use == 'c':
		print "%s closes backpack..." % name
		pause('^^^')
	elif use in ('flashlight', 'flash', 'fl'):
		if flash == True:
			pause('...')
			print "As %s shines the light across the walls, a strange noise can" % name
			print "be heard through the door...\n"
			backpack()
		else:	
			flash = True
	elif use == 'energy bar' and bars == True:
		pause('[##]')
		health(10)
		bp.remove('energy bar')
		bars = False
		backpack()
	elif use in ('sword', 'equip sword') and sword == 1:
		pause('++I====>')
		print "%s equips the %s!\n" % (name, bold('sword'))
		bp.remove('sword')
		sword = 3
		backpack()
	elif use in ('health','health monitor', 'hm'):
		pause(':::')
		health(0)
		pause(':::')
		backpack()
	elif use == 'potion' and potion > 0:
		pause(bold(blue('-OTO-')))
		get_potion(-1)
		backpack()
	elif use in ('tri','tri shield','equip tri shield') and tri == 1:
		pause('{}{}{}')
		print "%s equips the %s!\n" % (name, bold('tri shield'))
		bp.remove('tri shield')
		print "%s feels a rush of energy!" % name
		health(300)
		tri = 2
		backpack()
	elif use in ('hex', 'hex shield', 'equip hex shield') and hex == 1:
		pause('{}{}{}')
		print "%s equips the %s!\n" % (name, bold('hex shield'))
		bp.remove('hex shield')
		print "%s feels a rush of energy!" % name
		health(600)
		hex = 2
		backpack()
	else:
		print red("\n**Please try again**\n")
		backpack()

def get_potion(amt):
	global potion
	if amt > 0:
		print blue("+++%s POTIONS+++" % amt)
		potion += amt
		for pots in range(amt):
			bp.append('potion')
	else:
		print "%s takes a " % name + bold(blue("POTION"))
		health(30)
		potion -= 1
		bp.remove('potion')
			
def beastatt(type1, hits):
	time.sleep(.5)
	pause(bold('V--V'))
	print "The %s retaliates for" % type1 + red(" %d DAMAGE!\n\n") % hits
	health(-hits)

def fight(type, hit, min, max):
	global sword
	global healthp
	global potion
	global bp
	beast = hit
	pause('#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#')
	if sword == 3:
		minA = 10
		maxA = 40
		attword = 'slashes'
		print "\nWith sword in hand, %s stands ready for the %s!\n" % (name, type)
	else:
		minA = 5
		maxA = 12
		attword = "hits"
		print "\nNot enough time to untie the sword from the backpack! Should have equiped it!\n"

 	while beast >= 0:
		print "%s's HEALTH: " % name + blue("%d") % healthp
		print "%s HEALTH: " % type + bold("%d") % beast
		swordh = random.randint(minA, maxA)
		beasth = random.randint(min, max)
		fight = raw_input("1. Attack  2. Flash  3. Potion >>> ")
		
		if fight in('1', 'attack', 'Attack'):
			print'\n'
			pause(bold('++I====>'))
			print "%s %s the %s for" % (name, attword, type) + red(" %d DAMAGE!\n") % swordh
			beast -= swordh
			if beast > 0:
				beastatt(type, beasth)
			else:
				print "%s strikes the %s DOWN!" % (name, type)
				print blue("****VICTORY****")
				get_potion(3)
		elif fight in ('2', 'flash', 'Flash'):
			if min != max:
				print '\n'
				pause(bold(yellow('<(--)>')))
				print "%s shines the flashlight into the %ss eyes, weakening it..." % (name, type)
				max -= 1
				print "%s attack" % type + bold(" DOWN\n")
				beastatt(type, beasth)
			else:
				print'\n'
				pause('---')
				print "Can't weaken anymore.\n"
				beastatt(type, beasth)
		elif fight in ('3', 'potion', 'Potion'):
			if potion >= 1:
				print '\n'
				pause(bold(blue('-OTO-')))
				print "%s takes a " % name + bold(blue("POTION"))
				health(30)
				potion -= 1
				bp.remove('potion')
				beastatt(type, beasth)
			else:
				print '\n'
				pause('000')
				print "No potions!!!\n"
		else:
			print '\n'
			pause(bold('<==>'))
			print "The %s grabs at %s in a fit of rage." % (type, name)
			health(-2)

def pause(sym):
	for dots in range(3):
		print sym
		time.sleep(.2)
		
def die(why):
	pause(red('(XX)'))
	print why
	print red('\n***GAME OVER***\n')
	sys.exit(0)
	
def health(hit):
	global healthp
	if hit > 0:
		print blue("\nPLUS %d health!" % hit)
		healthp += hit
		print "HEALTH: %d\n" % healthp
	elif hit == 0:
		print "\nHEALTH: %d\n" % healthp
	else:
		time.sleep(1)
		print red("%s takes %d DAMAGE!\n") % (name, hit)
		healthp += hit
		if healthp <= 0:
			die('%s takes a mortal BLOW!' % name)
			sys.exit(0)

def flashlight(expose):
	#NOT GOING TO USE THIS
	print "\n%s shines the flashlight around the dark room ands sees a %s." % (name, expose)
	pickup = raw_input("Pick items up?[Y/N] ")
	if pickup in ('y', 'Y'):
		print "\n%s picks up %s." % (name, bold(expose))
		bp.append(expose)
	else:
		print "\n%s leaves the %s on the ground.\n" % (name, bold(expose))

def get_chest():	
	global triangle
	global square
	global healthp
	global chest
	comb = ['2', '4', '1', '3']
	ans = []
	print "The chest is locked and has four colored switches on it:\n"
	print green("[1GREEN]"), yellow("[2YELLOW]"), red("[3RED]"), blue("[4BLUE]\n")
	for nums in comb:
		press = raw_input('Which switch should %s press? ' % name)
		ans.append(press)
	if ans == comb:
		pause('+++')
		print "The chest suddenly pops open! There is a hexagon key and a triangle key...\n"
		choo = raw_input('Which one should %s take? ' % name)
		if choo in ('t', 'triangle', 'the triangle'):
			pause('...')
			print "%s takes the triangle shaped key and the chest snaps shut!\n" % name
			triangle = True
			chest = False
		elif choo in ('h', 'hexagon', 'the hexagon'):
			pause('...')
			print "%s takes the hexagon shaped key and the chest snaps shut!\n" % name
			square = True
			chest = False
		else:
			pause('...')
			print "The chest snaps shut!\n"
			get_chest()
	else:
		print "\nThe chest shocks %s!" % name
		health(-10)
		room2()

def room1():
	global flash
	global sword
	repeat1 = '''%s looks around the room again and sees a piece of paper with the 
word %s written on it. A door with a combination lock on it. And a 
broken stone slab with writing on it. Perhaps %s should 'inspect' the slab.
''' % (name, bold("'D E A T H'"), name)
	y = 1
	code = ['4', '5', '1', '20', '8']
	user = []
	step1 = raw_input(prompt)
	if step1 == 'b':
		pause('^^^')
	if step1 in ('inspect door', 'door', 'inspect the door'):
		pause('...')
		print "There is a lock with 5 numbered slides on it, each slide has 26 numbers..."
		for nums in range(5):	
			c = raw_input("Move slide %d to: " % y)
			user.append(c)
			y += 1
		if user == code:
			pause('+++')
			print "The door slowly opens..."
			flash = 0
			pause('...')
			print "Upon entering the next room, something starts moving towards %s!" % name
			print "Where did that flashlight go?! Its coming up FAST!"
			print "Grab the flashlight from the backpack! "
			pause('^^^')
			backpack()
			if flash == 1:
				print "\nCovered in grotesque boils and mold, a beast 7 feet tall screams and backs"
				print "away from the light before continuing the charge!\n"
				fight('Beast', 200, 2, 7)
			else:
				die('%s barely screams while being torn to shreds by the unkown beast!' % name)
			pause('...')
			print '''A little shaken from the fight, %s backs away from the downed creature 
and shines the flashlight around the room. There is a door on the left 
and one on the right with strange looking holes where the locks should 
be. A small chest sits in the middle of the room with the word %s 
written in red on the wall above it. In one corner, is 
something covered with a sheet.\n''' % (name, red("LAST"))
			room2()
		else:
			print "Nothing happens and %s backs away from the door..." % name
			pause('...')
			room1()
	elif step1 == 'inspect':
		pause('...')
		print "%s must choose something to inspect...\n" % name	
		room1()
	elif step1 in ('h', 'H', 'help'):
		pause('...')
		help()
		room1()
	elif step1 in ("inspect slab","slab", 'inspect the slab'):
		pause('...')
		print '%s takes a closer look at the slab. A lot of it is missing:' % name
		print bold('''\t\t...............
		....... j10 k11
		l12 m13 n14....
		q17 r18........
		v22............''')
		time.sleep(2)
		if sword == 0:
			print "%s touches the slab and a sword comes clattering out from behind" % name 
			print "the stone!"
			print "\n%s recieves %s!\n" % (name, bold('sword'))
			bp.append('sword')
			sword = 1
			room1()
		else:
			room1()
	elif step1 == 'b':
		backpack()
		room1()
	elif step1 == 'l':
		pause('...')
		print repeat1
		room1()
	elif step1 in ('paper', 'inspect paper', 'inspect the piece of paper', 'piece of paper'):
		pause('...')
		print "%s picks up the piece of paper. There doesn't appear to be anything else on it.\n" % name
		room1()
	else:
		pause('...')
		print "%s stands there rigid with fear...\n" % name
		room1()

def room2():
	global triangle
	global square
	global chest
	global sheet
	global flash
	paper = bold('''The paper reads...
	"The 'yellow' beast came charging out of the forest first. It was soon 
	followed by a warrior wearing 'blue' armor. The warrior let out a cry 
	before heaving a 'green' spear at the beast..."\n
''')
	repeat2 = '''There is a door on the left and one on the right with strange looking holes 
where the locks should be. A small chest sits in the middle of the room 
with the word %s written in red on the wall above it. In one corner, 
is something covered with a sheet.\n''' % red("LAST")
	act = raw_input(prompt)
	if act == 'b':
		pause('^^^')
		backpack()
		room2()
	elif act == 'l':
		pause('...')
		if sheet == True:
			print repeat2
		else:
			print repeat2[:-32] + 'a piece of paper...\n'
		room2()
	elif act in ('h', 'H', 'help'):
		pause('...')
		help()
		room2()
	elif act in ('corner', 'inspect corner', 'sheet', 'inspect sheet') and sheet == True:
		pause("...")
		print "%s pulls the sheet away to find a potion and a piece of paper...\n" % name
		get_potion(1)
		print paper
		sheet = False
		room2()
	elif act in ('corner','inspect corner','paper','inspect paper','inspect the corner','inspect the paper') and sheet == False:
		pause("...")
		print paper
		room2()
	elif act in ('chest', 'inspect chest'):
		pause('...')
		if chest == True:
			get_chest()
			room2()
		else:
			print "The switches on the chest have dissolved and it looks locked for good...\n"
			room2()
	elif act in ('left door', 'inspect left', 'inspect left door', 'ld'):
		if triangle == True:
			print '\nThe left door slowly opens...'
			pause('+++')
			print '''The new room %s walks into is pitch dark. %s feels along 
the walls to find the room is in the shape of a triangle, doesn't 
appear to have a door besides the one %s came in, and has small 
knobs on each of the walls.\n''' % (name, name, name)
			flash = False
			leftroom()
		else:
			pause('...')
			print 'The door appears to have a triangle shaped lock on it...'
			time.sleep(2)
			print "%s walks away from the door to check out the rest of the room." % name
			pause('...')
			room2()
	elif act in ('right door', 'inspect right', 'inspect right door', 'rd'):
		if square == True:
			print 'The right door slowly opens...'
			pause('+++')
			print '''The new room %s walks into is in the shape of a hexagon and has a
single door with a strange imp dancing in front of it. The room 
is well lit and the imp doesn't look too threatening so %s 
approaches it.\n''' % (name, name)
			rightroom()
		else:
			pause('...')
			print 'The door appears to have a hexagon shaped lock on it...'
			time.sleep(2)
			print "%s walks away from the door to check out the rest of the room." % name
			pause('...')
			room2()
	else:
		pause('...')
		print "%s contemplates what to do...\n" % name
		room2()
		
def rightroom():
	global bp
	global hex
	boss = '''%s slowly walks into the room. There are candles lit and jars with 
strange bits of flesh and body parts in them. There is a door in 
the back and a chest in the middle of the room.\n''' % name
	repeatrr = '''%s looks around the hexagon shaped room. A chill goes through %s's 
spine looking at the dancing imp\n''' % (name, name)
	
	print bold("'Hello there,'"), "says the Imp."
	time.sleep(1)
	print bold("'Guess my name and I shall let you pass to see my master!'"), "the Imp laughs.\n"
	time.sleep(1)
	step1000 = raw_input(prompt)
	
	if step1000 == 'b':
		pause('^^^')
		backpack()
		rightroom()
	elif step1000 in ('h', 'H', 'help'):
		pause('...')
		help()
		rightroom()
	elif step1000 == 'l':
		pause('...')
		print repeatrr
		rightroom()
	elif step1000 in ('inspect imp','Imp','imp','inspect the imp','talk to imp','talk','talk to the imp'):
		pause('...')
		print bold("'I shall only give you six guesses or fight we will.'\n")
		for guess in range(6):
			gu = raw_input("Whats the imps name? ")
			if gu in ('Six', 'six'):
				pause(bold(green("\<(#)#)>/")))
				print bold("'NOOOOO,'"), "shrieks the imp."
				time.sleep(1)
				print bold("'My master will not be happy!'"), "it groans."
				time.sleep(1)
				pause('{}{}{}')
				print "The Imp melts into a hexagon shaped shield and the door slowly"
				print "starts sliding open..."				
				print "%s recieves %s!\n" % (name, bold('hex shield'))
				bp.append('hex shield')
				hex = 1
				get_potion(3)
				print '\n'
				print boss
				bossroom()
			else:
				pause(green(bold('\<@@>/')))
				print bold("'Not quite,'"), "cackles the Imp.\n"
		fight('Imp', 300, 4, 15)
		print boss
		bossroom()
	elif step1000 in ('attack', 'attack the imp', 'attack imp'):
		pause('...')
		print "%s lunges at the Imp!\n" % name
		fight('Imp', 300, 5, 10)
		pause('{}{}{}')
		print "%s recieves %s!\n" % (name, bold('tri shield'))
		bp.append('tri shield')
		tri = 1
		print boss
		bossroom()
	else:
		pause('...')
		print repeatrr
		rightroom()
	
def leftroom():
	global tri
	repeatlr = '''The room is pitch dark. %s feels along the walls to find the room is in 
the shape of a triangle, doesn't appear to have a door besides the one 
%s came in and has small knobs on each of the walls.\n''' % (name, name)
	stEP = raw_input(prompt)
	if stEP == 'b':
		pause('^^^')
		backpack()
		if flash == True:
			pause(bold(yellow('(oo)')))
			print "%s flashes the light around the room, the knobs light up and a door" % name
			print "appears on the floor. A gigantic muscular imp crawls out and starts"
			print "moving towards %s!\n" % name
			fight('Giant Imp', 300, 4, 11)
			pause('{}{}{}')
			print "The Giant Imp melts into a triangle shaped shield and the door slowly"
			print "starts sliding open..."
			pause('+++')
			print "%s recieves %s!\n" % (name, bold('tri shield'))
			bp.append('tri shield')
			tri = 1
			print'''%s slowly walks into the room. There are candles lit and jars with 
strange bits of flesh and body parts in them. There is a door in 
the back and a chest in the middle of the room.\n''' % name
			bossroom()
		else:	
			leftroom()
	elif stEP in ('h', 'H', 'help'):
		pause('...')
		help()
		leftroom()
	elif stEP == 'l':
		pause('...')
		print repeatlr
		leftroom()
	elif stEP in ('inspect knobs', 'knobs', 'inspect the knobs'):
		pause('...')
		print "%s touches one of the knobs, its feels like some sort of prism..." % name
		pause('...')
		leftroom()
	else:
		print repeatlr
		leftroom()
		
def bossroom():
	repboss = '''%s slowly walks around the room. There are candles lit and jars with 
strange bits of flesh and body parts in them. There is a door in 
the back and a chest in the middle of the room.\n''' % name
	
	last = raw_input(prompt)
	if last == 'b':
		pause('^^^')
		backpack()
		bossroom()
	elif last == 'l':
		pause('...')
		print repboss
		bossroom()
	elif last in ('h', 'H', 'help'):
		pause('...')
		help()
		bossroom()
	elif last in ('inspect chest', 'chest', 'inspect the chest'):
		pause('...')
		print "%s opens the chest to find 5 potions!\n" % name
		get_potion(5)
		print bold("\nThe door in the back of the room bursts open and a tall terrifying looking")
		print bold("Wizard comes flying out!")
		if tri == 2:
			pause(bold('%^%'))
			print "%s feels the energy from the tri shield repeling the wizard!" % name
			print "The Wizard loses 1/4 of his power!\n"
			fight('Wizard', 600, 15, 30)
			end()
		elif hex == 2:
			pause(bold('%^%'))
			print "%s feels the energy from the hex shield repeling the wizard!" % name
			print "The Wizard loses half of his power!\n"
			fight('Wizard', 600, 10, 20)
			end()
		else:
			pause(bold('%^%'))
			print "%s has no shield equipped! The Wizard attacks with full force!\n" % name
			fight('Wizard', 600, 20, 40)
			end()
	elif last in ('inspect door', 'door', 'inspect the door'):
		pause('...')
		print 'The door appears to be locked...\n'
		bossroom()
	else:
		pause('...')
		print repboss
		bossroom()
		
def end():
	pause('*****************')
	print "%s defeats the Wizard and finds a shaft leading up to the surface!" % name
	pause('*****************')
	print bold("THE FUCKING END :D")
	pause('*****************')
	sys.exit(0)

bp = ['flashlight', 'energy bar', 'health monitor']
bars = True
sword = 0
potion = 0
flash = False
healthp = 100
triangle = False
square = False
chest = True
sheet = True
hex = 0
tri = 0
	

print bold('''
##################################################################
#   ____   _  _  _  _  __  ____  __  _  _                        #
#   |   \  |  |  |\ | /  \ |    /  \ |\ |   ZERO ZERO ZERO ZERO  #
#   |   |  |  |  | \| | __ |--  |  | | \|   ZERO ZERO ZERO ZERO  #
#   |___/  \__/  |  | \__/ |___ \__/ |  |   ZERO ZERO ZERO ZERO  #
#                                                                #
##################################################################
                                                 Copyright AB Inc.''')

name = raw_input('Choose a name: ')
name = bold(name)
prompt = "What should %s do([h] for help)? " % name

pause('...')
print '''In a backpacking trip across the Himalayas gone wrong, %s is suddenly 
falling and sliding into a deep pit! Finally landing in a pile of 
sand, %s, dazed and confused, looks around the strange new place. 
Perhaps there might be a flashlight in the backpack.''' % (name, name)
	
pause('^^^')
backpack()

if flash == 1:
	pause('...')
	print '''%s flashes the light around the room and sees a piece of paper with the 
word %s written on it. A door with a combination lock on it. And a 
broken stone slab with writing on it. Perhaps %s should 'inspect' the slab.\n''' % (name, bold("'D E A T H'"), name)
else:
	tries = 0
	die('%s stumbles around in the dark and falls in a pit...\n' % name)
	
room1()