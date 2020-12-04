#!/usr/bin/python3
# coding: utf-8


def affRestosNuits( lstNbRestos ) :
	
	for i in range( len(lstNbRestos) ) :
		numJour = i + 1
		print( "Nuit du" , numJour , ":" , lstNbRestos[ i ] )
		
		
def corrigerDonnees( lstNbRestos ) :
	
	cpt = 0
	
	for i in range( len( lstNbRestos ) ) :
		
		if lstNbRestos[ i ] < 0 :
			lstNbRestos[ i ] = 0
			cpt = cpt + 1
			
		elif lstNbRestos[ i ] > 331 :
			lstNbRestos[ i ] = 331
			cpt = cpt + 1
			
	return cpt
		
	
	

if __name__ == "__main__" :

	ouvertsParisNuit = [ 
			103 , 89 , 45 , 82 , 35 , 101 , 159 , 23 , 32 , -72 , 
			-523 ,  86 , 27 , 102 , 203 , 109 , 27 , 92 , 102 , 92 ,
			72 , 90 , 23123123 , 25 , -2383 , 9 , 28 , 33 , 90 , 83
		]
	
	print( "--- Avant correction ---\n" )
	affRestosNuits( ouvertsParisNuit )
	print( "------------------------\n" )
	
	nbCorrections = corrigerDonnees( ouvertsParisNuit )
	print( nbCorrections , "valeurs ont dû être corrigées." )
	
	print( "\n--- Après correction ---\n" )
	affRestosNuits( ouvertsParisNuit )
	print( "------------------------\n" )
	
	
	
