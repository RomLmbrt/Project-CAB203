import borkAutomator
bork = borkAutomator.Bork()

# Some helper functions used later in traverseBork and traverseBorkHardCore

#Return True if the exit endpoint is not in map
def exitNotInMap(exit, map):
    count = 0
    for elt in map :
        if elt == exit :
            count+=1
    return (count == 0)

#Return True if there is at least one exit endpoint in exits that is not in map
def exitsNotInMap(exits, map):
    count = 0
    for exit in exits :
        if ( exitNotInMap(exits[exit], map) ):
            count+=1
    return (count != 0)

#The main functions

#Return the map in normal mode
def traverseBork(bork):
    bork.restart()
    saveGame=bork.save()
    map={}
    
    #Recursive function that visits the unvisited spots 
    #or comes back if there is no more unvisited spot remaining from the very location
    
    def visiteOrCallback(map, saveGame):
        newSaveGame = bork.save()
        location = bork.description()
        map[location]={}
        
        #Add the exits to the very location in map
        for exit in bork.exits() :
            bork.move(exit)
            map[location][exit] = bork.description()
            bork.restore(newSaveGame)
            
        #Moves to the next unvisited spots
        while exitsNotInMap(map[location], map ):
            for exit in map[location]:
                if (exitNotInMap(map[location][exit], map)):
                    bork.move(exit)
                    visiteOrCallback(map, newSaveGame)
                     
        #Comes back to the last spot
        bork.restore(saveGame)
    
    visiteOrCallback(map, saveGame)

    return map

# The hard core mode

#Return the map in hard core mode
def traverseBorkHardCore(bork):
    bork.restart()
    map={}
    memory=[]
    
    #Recursive function that visits the unvisited spots 
    #or comes back if there is no more unvisited spot remaining from the very location
   
    def visiteOrCallbackHC(map, memory):
        location = bork.description()
        map[location]={}
        
        #Add the exits to the very location in map
        for exit in bork.exits() : 
            bork.move(exit)
            map[location][exit] = bork.description()
            #Come back to the last spot
            bork.restart()
            for exit in memory :
                bork.move(exit)
            
        #Moves to the next unvisited spots
        while ( exitsNotInMap(map[location], map ) == True ) :
            for exit in map[location]:
                if (exitNotInMap(map[location][exit], map)):
                    bork.move(exit)
                    memory.append(exit)
                    visiteOrCallbackHC(map, memory)
                     
        #Comes back to the last spot
        if memory!=[]:
            memory.pop()
        bork.restart()
        for exit in memory :
            bork.move(exit)
       
    
    visiteOrCallbackHC(map, memory)

    return map

# Run traverseBork and traversBorkHardCore

print(traverseBork(bork))

try:
    borkHC = borkAutomator.Bork(hardCore=True)
    print(traverseBorkHardCore(borkHC))
except NameError:
    print("Not attempting hard core mode")

