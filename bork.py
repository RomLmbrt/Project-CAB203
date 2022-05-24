def traverseBork(bork):
    
    def notInMap(exits, map):
        count = 0
        for exit in exits :
            k = 0
            for elt in map :
                if elt == exit :
                    k+=1
            if ( k==0 ) :
                count +=1
        return (count != 0)

    def visiteOrCallback(map, location, saveGame):
        map[location]={}
        for exit in bork.exits() :
            map[location][exit]=""
        newSaveGame = bork.save()
        #something to visit
        while ( notInMap(map[location], map ) == True ) :
            for exit in map[location] :
                bork.move(exit)
                map[location][exit] = bork.description()
                bork.restore(newSaveGame)
                if (notInMap(exit, map)):
                    bork.move(exit)
                    visiteOrCallback(map, exit, newSaveGame)
        #nothing to visit
        bork.restore(saveGame)
        
   # code your solution here
    bork.restart()
    location = bork.description()
    saveGame = bork.save()
    map={}
    
    visiteOrCallback(map, location, saveGame)
    
    return(map)
            
   # Access the bork automator like so:
   bork.restart()
   location = bork.description()
   exits = bork.exits()
   exit = "???"
   bork.move(exit)
   saveGame = bork.save()
   bork.restore(saveGame)

   # Access functions from the imported files like this:
   n = graphs.N(V, E, u)
   t = digraphs.topOrdering(V, E)

   return map

# The following will be run if you execute the file like python3 bork_n1234567.py
# Your solution should not depend on this code.
if __name__ == "__main__":
   import borkAutomator
   bork = borkAutomator.Bork()
   print(traverseBork(bork))

   try:
      borkHC = borkAutomator.Bork(hardCore=True)
      print(traverseBorkHardCore(borkHC))
   except NameError:
      print("Not attempting hard core mode")
