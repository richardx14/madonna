from random import randint

# songs = ["Beautiful Stranger", "True Blue", "Vogue", "Lucky Star"]

def getASong():

	print("Getting a song.")

	songList = createSongList()

	if songList:
		foo2 = randint(0,len(songList)-1 )
		songOfTheDay = songList[foo2]
		print("Song of the day is " + songOfTheDay + ".")
		del songList[foo2]
		#print("remaining songs = " + str(songList))
		return(songOfTheDay)

	else:
		print("Madonna has run out of songs!")
		return("Madonna has run out of songs!")

def createSongList():

	songs = [
	"4 Minutes",
	"American Life",
	"B-Day Song",
	"Bad Girl",
	"Beat Goes On",
	"Beautiful Killer",
	"Beautiful Stranger",
	"Bedtime Story",
	"Best Friend",
	"Bitch I'm Madonna",
	"Body Shop",
	"Borderline",
	"Burning Up",
	"Candy Store",
	"Celebration",
	"Cherish",
	"Crazy For You",
	"Dance Tonight",
	"Dear Jessie",
	"Deeper and Deeper",
	"Devil Pray",
	"Devil Wouldn't Recognize You",
	"Die Another Day",
	"Don't Tell Me",
	"Dress You Up",
	"Erotica",
	"Everybody",
	"Express Yourself",
	"Falling Free",
	"Frozen",
	"Future Lovers",
	"Gang Bang",
	"Get Together",
	"Ghosttown",
	"Girl Gone Wild",
	"Give it 2 Me",
	"Give Me All Your Luvin'",
	"Holiday",
	"Holy Water",
	"Human Nature",
	"Hung Up",
	"I Don't Give A",
	"I Fu--ed Up",
	"I Love New York",
	"I'll Remember",
	"I'm a Sinner",
	"I'm Addicted",
	"Iconic",
	"Illuminati",
	"Incredible",
	"Into The Groove",
	"Joan Of Arc",
	"Justify My Love",
	"La Isla Bonita",
	"Like A Prayer",
	"Like A Virgin",
	"Live To Tell",
	"Living For Love",
	"Love Song",
	"Love Spent",
	"Lucky Star",
	"Masterpiece",
	"Material Girl",
	"Miles Away",
	"Mother and Father",
	"Music",
	"Nothing Really Matters",
	"Oh, Father",
	"One More Chance",
	"Open Your Heart",
	"Papa Don't Preach",
	"Promise To Try",
	"Rain",
	"Ray Of Light",
	"Rebel Heart",
	"Rescue Me",
	"Revolver",
	"She's Not Me",
	"Some Girls",
	"Spanish Lessons",
	"Substitute For Love",
	"Superstar",
	"Take A Bow",
	"The Power Of Goodbye",
	"This Used To Be My Playground",
	"True Blue",
	"Turn Up the Radio",
	"Unapologetic Bitch",
	"Veni Vidi Vici",
	"Vogue",
	"Voices",
	"Wash All Over Me",
	"What It Feels Like For A Girl",
	"Who's That Girl",
	"You'll See"]

	return(songs)

def storeASong (song):
	storedSongs = []
	storedSongs.append(song)






