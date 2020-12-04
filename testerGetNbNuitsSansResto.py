#!/usr/bin/python3
# coding: utf-8


def getNbNuitsSansResto( lstNbRestos ) :
	
	cpt = 0
	
	for n in lstNbRestos :
		if n == 0 :
			cpt = cpt + 1
			
	return cpt
	


if __name__ == "__main__" :

	ouvertsParisNuit = [ 
			103 , 89 , 45 , 82 , 35 , 101 , 159 , 23 , 32 , 0 , 
			0 ,  86 , 27 , 102 , 203 , 109 , 27 , 92 , 102 , 92 ,
			72 , 90 , 0 , 25 , 175 , 9 , 28 , 33 , 90 , 83
		]
	
	nbSans = getNbNuitsSansResto( ouvertsParisNuit )
	
	print( "Ce mois, il y a eu" , nbSans , "nuits sans aucun restaurant ouvert." )
	
