#!/usr/bin/python3
# coding: utf-8


def getNom( unResto ) :
    ( nom , arrondissement ) = unResto.split( ':' )
    return nom

def getArrondissement( unResto ) :
    ( nom , arrondissement ) = unResto.split( ':' )
    return int( arrondissement )


def getArrondissementsAvecRestos( ) :
    global restos
    lesArr = []

    for unResto in restos:
        numArr = getArrondissement(unResto)
        if numArr not in lesArr :
            lesArr.append( numArr )

    return lesArr

def getArrondissementsSansRestos( ) :
    global restos
    lesArr = []

    # VOTRE CODE ICI

    return lesArr


if __name__ == '__main__' :

    restos = [
        'Turkish snack:11' ,
        'Tour Food:7' ,
        'Restaurant Gül:11' ,
        'Kebab House:11' ,
        'Apollon:7' ,
        'Zarma:9' ,
        'Restaurant Alim:11' ,
        'Art Kebab:7' ,
        'Coriandre:7' ,
        'Pacha kebab:9' ,
        'Paristanbul:7' ,
        'Restaurant Efes:11' ,
        'Firat:11' ,
        'Paristanbul:2' ,
        'Restaurant Dilan:2' ,
        'Pacha kebab:11' ,
        'Mac Doner:11' ,
        'Le Giros:7' ,
        'Chez Yamina:9' ,
        'Pita Kebab:1' ,
        'Al Boustan:1' ,
        'Le Bosphore:1' ,
        'Planet Istanbul:11' ,
        'Istanbul kebab:11' ,
        'Diyar:7' ,
        'Nabab Kebab:1' ,
        'Grillé:2' ,
        'Chilane:7'
    ]

    lesArrSans = getArrondissementsSansRestos()

    for unArrSans in lesArrSans :
        print( unArrSans )
