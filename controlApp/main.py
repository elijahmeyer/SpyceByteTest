
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
    print("Creating spice...")
    test = Spice.Spice(4, "weed", 2, 5, "This is actually just oregano")
    print("Saving spice...")
    saveSpice(test)
    return 0

# Saves information of the spice in the form of a tuple in a text file.
# This tuple is structured as follows: (id,name,dispenserInfo,sensorInfo,blend)
# The file will be saved to spiceConfig.txt in the same directory as main function.
def saveSpice(spice):
	print(type(spice))
	if type(spice) is Spice.Spice:
		outfile = open(".\spiceConfig.txt", "w")
		outfile.write("%s,%s,%s,%s,%s" % (spice.getID(), spice.getName(), spice.getDispenserInfo(), spice.getSensorInfo(), spice.getBlend()))
		outfile.close()
		print("Save Successful!")
	return 0
	
if __name__ == '__main__':
    main()
#    import sys
#    sys.exit(main(sys.argv))
