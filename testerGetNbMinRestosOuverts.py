#!/usr/bin/python3
# coding: utf-8


def getNbMinRestosOuverts( lstNbRestos ) :
	
	nbMin = lstNbRestos[ 0 ]
	
	for n in lstNbRestos :
		if n < nbMin :
			nbMin = n
			
	return nbMin
	


if __name__ == "__main__" :

	ouvertsParisNuit = [ 
			103 , 89 , 45 , 82 , 35 , 101 , 159 , 23 , 32 , 3 , 
			4 ,  86 , 27 , 102 , 203 , 109 , 27 , 92 , 102 , 92 ,
			72 , 90 , 3 , 25 , 175 , 9 , 28 , 33 , 90 , 83
		]
	
	nbMin = getNbMinRestosOuverts( ouvertsParisNuit )
	
	print( "Ce mois, le nombre minimum de restaurants ouverts en une nuit est de" , nbMin , "." )
