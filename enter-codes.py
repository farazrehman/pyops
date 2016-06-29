

import menu
import pickle

print "Welcome to IATA code program"

# Globals
DAT_FILE = "data.csv"
TITLE = "**** IATA Assigned Airport Codes ****"
CONT = "Press any key to continue..."
LIST = {}

def checkEx():
	print "In checkEx()..."
	act = raw_input (CONT)
	
def addNew():
	print "In addNew()"
	print "Database will be appended"
	code = "m"
	while code !="qqq":
			code = raw_input ("Enter IATA Code:         ")
			name = raw_input ("Enter City/Airport Name: ")
			LIST [code] = name	
	
	act = raw_input (CONT)
	
def reInit():
	print "In ReInit()..."
	print "WARNING!!! EXISTING DATABASE WILL BE OVERWRITTEN"
		
	confirm = raw_input ("Enter YES to continue...")
	if confirm == "YES":		
		LIST = {}
						
	act = raw_input (CONT)
	
def display():
	for code in LIST:
		print code+" : "+LIST[code]
		
	act = raw_input (CONT)
		
		
	
def exit():
	print "In exit()..."
	print raw_input (CONT)
	
def loadDB():
	print "Loading database...please wait..."
	dbf = open (DAT_FILE, "a")

loadDB()

mainMenu = menu.Menu(TITLE)

options = [{"name":"Check if code exist","function":checkEx},
           {"name":"Add New Codes","function":addNew},
           {"name":"Re-Initialize DB","function":reInit},
           {"name":"Print database","function":display},
           {"name":"Exit","function":exit}]
mainMenu.addOptions(options)


mainMenu.open()








