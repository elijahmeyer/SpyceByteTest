class Spice():
	
	def __init__(self, spiceID, name, dispenserInfo, sensorInfo, blend=""):
		self.spiceID = spiceID
		self.name = name
		self.dispenserInfo = dispenserInfo
		self.sensorInfo = sensorInfo
		self.blend = blend
		self.fullness = self.readSensor()
	
	def getID(self):
		return self.spiceID
		
	def setID(self, spiceID):
		self.spiceID = spiceID
		
	def getName(self):
		return self.name
	
	def setName(self, name):
		self.name = name
	
	def getDispenserInfo(self):
		return self.dispenserInfo
	
	def setDispenserInfo(self, dispenserInfo):
		self.dispenserInfo = dispenserInfo
	
	def getSensorInfo(self):
		return self.sensorInfo
	
	def setSensorInfo(self, sensorInfo):
		self.sensorInfo = sensorInfo
		
	def getBlend(self):
		return self.blend
		
	def setBlend(self, blend):
		self.blend = blend
	
	def getFullness(self):
		return self.fullness
	
	def dispense(self, quarterTsp):
		print("Dispensing %d quarter teaspoons!" % quarterTsp)
		print("Coming Soon: Actual dispensing functionality.")
		
	def readSensor(self):
		print("Coming Soon: Actual functioning sensors!")
		return 0
	
	def toString(self):
		return "ID: %s\nName: %s\nDispenser: %s\nSensor: %s\nBlend: %s\n" % (self.getID(), self.getName(), self.getDispenserInfo(), self.getSensorInfo(), self.getBlend()) 

#test = Spice(42, "Spaghetti", "This is the dispenser info", "This is the sensor infor", "This is spaghetti, I don't know what you want.")
#print(test.getName())
#test.setName("Sp4gh3tt1")
#print(test.getName())
#print(test.getBlend())
#test.setBlend("OK, it's linguini now.")
#print(test.getBlend())
#print(test.getFullness())
#test.dispense(6)
#test.readSensor()
#print(type(test))
