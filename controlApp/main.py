
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2019 elija <elija@DESKTOP-18RS6LS>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import Spice

def main():
    print("Creating spices...")
    test1 = Spice.Spice(4, "oregano", 2, 5, "This is just oregano")
    test2 = Spice.Spice(4, "salt", 1, 1, "Salt")
    test3 = Spice.Spice(6, "other spice", 3, 3, "I need to learn more spices")
    jars = [test1, test2, test3]
    print("Saving spice...")
    saveSpice(jars)
    print("Loading spice...")
    load1 = Spice.Spice(0, "", 0, 0, "")
    load2 = Spice.Spice(0, "", 0, 0, "")
    load3 = Spice.Spice(0, "", 0, 0, "")
    loadJars = [load1, load2, load3]
    loadSpices(loadJars)
    for jar in loadJars:
        print(jar.toString())
    return 0

# Saves information of the spice in the form of a tuple in a text file.
# This tuple is structured as follows: (id,name,dispenserInfo,sensorInfo,blend)
# The file will be saved to spiceConfig.txt in the same directory as main function.
def saveSpice(spice_list):
	outfile = open(".\spiceConfig.txt", "w")
	for spice in spice_list:
		if type(spice) is Spice.Spice:
			outfile.write("%s~%s~%s~%s~%s\n" % (spice.getID(), spice.getName(), spice.getDispenserInfo(), spice.getSensorInfo(), spice.getBlend()))
			print("Save Successful!")
	outfile.close()
	return 0

def loadSpices(spice_list):
	try:
		infile = open(".\spiceConfig.txt", "r")
		for spice in spice_list:
			if type(spice) is Spice.Spice:
				spiceTuple = infile.readline().strip()
				index1 = spiceTuple.index('~')
				spiceID = spiceTuple[:index1]
				index2 = spiceTuple.index('~', index1+1)
				name = spiceTuple[index1+1:index2]
				index3 = spiceTuple.index('~', index2+1)
				dispenserInfo = spiceTuple[index2+1:index3]
				index4 = spiceTuple.index('~', index3+1)
				sensorInfo = spiceTuple[index3+1:index4]
				blend = spiceTuple[index4+1:]
				spice.setID(spiceID)
				spice.setName(name)
				spice.setDispenserInfo(dispenserInfo)
				spice.setSensorInfo(sensorInfo)
				spice.setBlend(blend)
		infile.close()
	except IOError:
		print("No save file found.")
		return 0
if __name__ == '__main__':
    main()
#    import sys
#    sys.exit(main(sys.argv))
