#!/usr/bin/python3
# coding: utf-8

def getNbMaxRestosOuverts( lstNbRestos ) :
	
	nbMax = lstNbRestos[ 0 ]
	
	for n in lstNbRestos :
		if n > nbMax :
			nbMax = n
			
	return nbMax
	


if __name__ == "__main__" :

	ouvertsParisNuit = [ 
			103 , 89 , 45 , 82 , 35 , 101 , 159 , 23 , 32 , 0 , 
			0 ,  86 , 27 , 102 , 203 , 109 , 27 , 92 , 102 , 92 ,
			72 , 90 , 0 , 25 , 175 , 9 , 28 , 33 , 90 , 83
		]
	
	nbMax = getNbMaxRestosOuverts( ouvertsParisNuit )
	
	print( "Ce mois, le nombre maximum de restaurants ouverts en une nuit est de" , nbMax , "." )
