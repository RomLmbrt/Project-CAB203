def traverseBork(bork):
    
    def exitsNotInMap(exits, map):
        count = 0
        for exit in exits :
            k = 0
            for elt in map :
                if elt == exits[exit] :
                    k+=1
            if ( k==0 ) :
                count +=1
        return (count != 0)
        
    def exitNotInMap(exit, map):
        count = 0
        for elt in map :
            if elt == exit :
                count+=1
        return (count == 0)

    def visiteOrCallback(map, saveGame):
        newSaveGame = bork.save()
        location = bork.description()
        map[location]={}
        for exit in bork.exits() :
            map[location][exit]=""
        for exit in map[location] :
            bork.move(exit)
            map[location][exit] = bork.description()
            bork.restore(newSaveGame)
        #something to visit
        while ( exitsNotInMap(map[location], map ) == True ) :
            for exit in map[location]:
                if (exitNotInMap(map[location][exit], map)):
                    bork.move(exit)
                    map = visiteOrCallback(map, newSaveGame)
        #nothing to visit
        bork.restore(saveGame)
        return(map)
        
   # code your solution here
    bork.restart()
    saveGame=bork.save()
    map={}
    
    visiteOrCallback(map, saveGame)
    
    return(map)
