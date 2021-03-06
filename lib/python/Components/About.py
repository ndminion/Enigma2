from Tools.Directories import resolveFilename, SCOPE_SYSETC
from enigma import getEnigmaVersionString
from os import popen

class About:
	def __init__(self):
		pass

	def getVersionString(self):
		return self.getImageVersionString()

	def getImageVersionString(self):
		try:
			file = open(resolveFilename(SCOPE_SYSETC, 'image-version'), 'r')
			lines = file.readlines()
			for x in lines:
				splitted = x.split('=')
				if splitted[0] == "version":
					#     YYYY MM DD hh mm
					#0120 2005 11 29 01 16
					#0123 4567 89 01 23 45
					version = splitted[1]
					year = version[-13:-9]
					month = version[-9:-7]
					day = version[-7:-5]
					name = version[1:-13]

					return '-'.join(([name, year, month, day]))
			file.close()
		except IOError:
			pass

		return "unavailable"

	def getEnigmaVersionString(self):
		return getEnigmaVersionString()

	def getKernelVersionString(self):
		try:
			result = popen("uname -r","r").read().strip("\n").split('-')
			kernel_version = result[0]
			return kernel_version
		except:
			pass

		return "unknown"

about = About()
