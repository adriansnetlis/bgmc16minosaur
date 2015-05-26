import bge

def getKey1(cont):
    key1 = bge.logic.globalDict.get("key1")
    if key1 is None:
        return
    cont.owner["key1"] = key1
  
def getHealth(cont):
    health = bge.logic.globalDict.get("health")
    if health is None:
        return
    cont.owner["health"] = health
    
    
def getStamina(cont):
    stamina = bge.logic.globalDict.get("stamina")
    if stamina is None:
        return
    cont.owner["stamina"] = stamina / 2