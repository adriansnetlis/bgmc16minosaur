import bge
from bge import logic

cont = logic.getCurrentController()
own = cont.owner

#info for me!!!
#States:
#0 - idling and seeking
#2 - run to player
#3 - attack player
#4 - breaking through door