def traverseBork(bork):
    def notInMap(exits, map):
       count = 0
       for exit in map :
          k = 0
          for elt in map :
             if elt == exit :
                k+=1
         if ( k!=0 ) :
            count +=1
      return (count == 0)
      
    def visiteOrCallback(map, location, saveGame):
        map[location]=bork.exits(location)
        newSaveGame = bork.save()
        #something to visit
        while ( !(notInMap(map[location], map )) ) :
           for exit in map[location] :
              if (notInMap(exit, map)):
            visiteOrCallback(map, exit, newSaveGame)
        #nothing to visit
        bork.restore(saveGame)
        
   # code your solution here
    location = bork.restart()
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
