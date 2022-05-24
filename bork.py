import graphs
import digraphs

# You can define some helper functions here if you like!

def traverseBork(bork):
   # code your solution here

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

# To play in hard core mode, define the function traverseBorkHardCore(bork)
# You shoud also define traverseBork either way!
# def traverseBorkHardCore(bork):

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
