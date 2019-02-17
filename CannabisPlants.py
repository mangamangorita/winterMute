##32 cannabis plants

from typeclasses.objects import Object
from evennia import create_object

class CannabisPlants(Object):
        """
    This object creates 32 cannabis plants in the grow room
        """

        def at_object_creation(self):

            self.db.desc = "Many dozens of man-sized cannabis plants "+
            "sag under their own weight.."

            cannaPlants = create_object("typeclasses.CannabisPlants.cannaPlants", 
                                        key="cannaPlants")
