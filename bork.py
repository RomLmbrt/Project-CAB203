def traverseBork(bork):
    
    def visiteOrCallback(map, location, saveGame):
        map[location]=bork.exits(location)
        newSaveGame = bork.save()
        #something to visit
        while there is a bork.exits(n) not in map :
            visiteOrCallback(map, bork.exits(n)[not in map], newSaveGame)
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
