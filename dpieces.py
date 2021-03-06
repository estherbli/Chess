import pieces 

#crée les pions
pionB1= pieces.pion( "blanc", 0, 1, 'pionB')
pionB2= pieces.pion( "blanc", 1, 1, 'pionB')
pionB3= pieces.pion( "blanc", 2, 1, 'pionB')
pionB4= pieces.pion( "blanc", 3, 1, 'pionB')
pionB5= pieces.pion( "blanc", 4, 1, 'pionB')
pionB6= pieces.pion( "blanc", 5, 1, 'pionB')
pionB7= pieces.pion( "blanc", 6, 1, 'pionB')
pionB8= pieces.pion( "blanc", 7, 1, 'pionB')

pionN1 = pieces.pion( "noir", 0, 6, 'pionN')
pionN2 = pieces.pion( "noir", 1, 6, 'pionN')
pionN3 = pieces.pion( "noir", 2, 6, 'pionN')
pionN4 = pieces.pion( "noir", 3, 6, 'pionN')
pionN5 = pieces.pion( "noir", 4, 6, 'pionN')
pionN6 = pieces.pion( "noir", 5, 6, 'pionN')
pionN7 = pieces.pion( "noir", 6, 6, 'pionN')
pionN8 = pieces.pion( "noir", 7, 6, 'pionN')

#crée les autres pièces blanches et noires
tourB1 = pieces.tour('blanc', 0, 0, 'tourB')
tourB2 = pieces.tour('blanc', 7, 0, 'tourB')
cavalierB1 = pieces.cavalier('blanc', 1, 0, 'cavalierB')
cavalierB2 = pieces.cavalier('blanc', 6, 0, 'cavalierB')
fouB1 = pieces.fou('blanc', 2, 0, 'fouB')
fouB2 = pieces.fou('blanc', 5, 0,'fouB')
dameB = pieces.dame('blanc', 3, 0, 'dameB') 
roiB = pieces.roi('blanc', 4, 0, 'roiB')

tourN1 = pieces.tour('noir', 0, 7, 'tourN')
tourN2 = pieces.tour('noir', 7, 7, 'tourN')
cavalierN1 = pieces.cavalier('noir', 1, 7, 'cavalierN')
cavalierN2 = pieces.cavalier('noir', 6, 7, 'cavalierN')
fouN1 = pieces.fou('noir', 2, 7, 'fouN')
fouN2 = pieces.fou('noir', 5, 7, 'fouN')
dameN = pieces.dame('noir', 3, 7, 'dameN') 
roiN = pieces.roi('noir', 4, 7, 'roiN')

Echiquier = {
    (0,0) : tourB1, (1,0) : cavalierB1, (2,0) : fouB1, (3,0) : dameB, (4,0) : roiB, (5,0) : fouB2, (6,0) : cavalierB2, (7,0) : tourB2,
    (0,1) : pionB1, (1,1): pionB2, (2,1) : pionB3, (3,1) : pionB4, (4,1) : pionB5, (5,1): pionB6, (6,1): pionB7, (7,1) : pionB8, 
    (0,7) : tourN1, (1,7) : cavalierN1, (2,7) : fouN1, (3,7) : dameN, (4,7) : roiN, (5,7) : fouN2, (6,7) : cavalierN2, (7,7) : tourN2,
    (0,6) : pionN1, (1,6): pionN2, (2,6) : pionN3, (3,6) : pionN4, (4,6) : pionN5, (5,6): pionN6, (6,6): pionN7, (7,6) : pionN8,
    }
