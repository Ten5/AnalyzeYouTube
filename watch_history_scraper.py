import json


class YtNode:
	def __init__(self, header: str, title: str, name: str) -> None:
		self.header = header
		self.title = title
		self.name = name


class Utilities:
	def readFile(fileName: str) -> dict:
		with open(fileName, 'r') as f:
			data = json.load(f)

		return data

	def writeToFile(fileName: str, data: any) -> None:
		file = open(fileName, 'w+')
		formatString = '{:50s} <--- {}'
		counter = 0

		if isinstance(data, list):
			for element in data:
				counter += 1
				file.write('{:5d}. {:20s} || {:100s} || {}'.format(counter, element.header, element.title, element.name))
				file.write('\n')

		else:
			for key in data:
				counter += 1
				file.write('{:5d}. {:50s} <--- {:10d}'.format(counter, key.strip(), data.get(key)))
				file.write('\n')

		file.close()

	def toPrintableMap(data: any) -> any:
		if isinstance(data, list):
			return sorted(data, key = lambda element: element.header)

		elif isinstance(data, dict):
			result = {}
			for item in data:
				result.update({item.header : {item.title : item.name}})

			return result



def parseFile(fileData: dict) -> list:
	ytStatList = []

	titleString = 'title'
	subtitleString = 'subtitles'
	headerString = 'header'

	for obj in fileData:
		header = ''
		title = ''
		name = ''

		if headerString in obj:
			header = obj[headerString]

		if titleString in obj:
			title = obj[titleString]

		if subtitleString in obj:
			subTitles = obj[subtitleString]
			name = subTitles[0]['name']

		ytObj = YtNode(header, title, name)
		ytStatList.append(ytObj)

		subTitles.clear()

	return ytStatList

def getArtistStats(data: list) -> dict:

	# ytMusicStats => Artist : List(Song)
	ytMusicStats = {}

	# artistFrequencyMap => Artist : No. of songs
	artistFrequencyMap = {}

	for element in data:
		key = element.name
		value = ytMusicStats.setdefault(key, [])
		value.append(element.title)

	# Sorts the keys on the basis of the values and returns a list of keys in a sorted manner
	for element in sorted(ytMusicStats, key = lambda values: len(ytMusicStats[values]), reverse = True):
		artistFrequencyMap.update({element : len(ytMusicStats[element])})

	return artistFrequencyMap

def sortDataByArtist(data: list) -> dict:
	data.sort(key = (lambda x: x.header))
	return getArtistStats(data)

def filterYtMusicData(data: list) -> list:
	return list(filter(lambda element: element.header == 'YouTube Music', data))

def filterYtData(data: list) -> list:
	return list(filter(lambda element: element.header == 'YouTube', data))

def getSongFrequency(data: list) -> dict:

	# ytSongFrequency => Song : Count
	ytSongFrequency = {}

	# orderedSongFreqMap => Decreasing Order (Song : Frequency)
	orderedSongFreqMap = {}

	for element in data:
		key = element.title.replace('Watched ', '')
		value = ytSongFrequency.setdefault(key, 0)
		ytSongFrequency[key] += 1

	# Sorts the keys on the basis of the values and returns a list of keys in a sorted manner
	for element in sorted(ytSongFrequency, key = lambda count: ytSongFrequency[count], reverse = True):
		orderedSongFreqMap.update({element : ytSongFrequency[element]})	

	return orderedSongFreqMap


def main() -> None:
	inFile = './watch-history.json'
	ytMusicStatsFile = './youtube_history_stats.txt'
	artistStatsFile = './ytMusicStats.txt'
	songsStatsFile = './ytSongStats.txt'

	fileData = Utilities.readFile(inFile)
	parsedData = parseFile(fileData)
	filteredYtData = filterYtData(parsedData)
	filteredYtMusicData = filterYtMusicData(parsedData)
	filteredYtRest = len(parsedData) - len(filteredYtData) - len(filteredYtMusicData)

	print('Stats:\n')
	print('Youtube: ' + str(len(filteredYtData)))
	print('Youtube Music: ' + str(len(filteredYtMusicData)))
	print('Youtube Rest: ' + str(filteredYtRest))

	artistData = sortDataByArtist(filteredYtMusicData)
	songsData = getSongFrequency(filteredYtMusicData)
	
	Utilities.writeToFile(artistStatsFile, artistData)
	Utilities.writeToFile(songsStatsFile, songsData)
	Utilities.writeToFile(ytMusicStatsFile, Utilities.toPrintableMap(parsedData))


main()