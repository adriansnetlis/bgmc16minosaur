import bge
from bge import logic

#info for me!!!
#armature states:
#0 = idle
#1 = walkFwd
#2 = runFwd
#3 = walkBck
#4 = runBack
#5 = turnLeft
#6 = turnRight
#7 = idleTired

#define controllers
cont = logic.getCurrentController()
own = cont.owner

keyboard = bge.logic.keyboard
scene = logic.getCurrentScene()
obj = scene.objects
armature = obj["CharacterArmature"]
ray = cont.sensors["ray"]

#define keyboard controllers
w_key = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.WKEY]
a_key = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.AKEY]
s_key = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.SKEY]
d_key = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.DKEY]
shift_key = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.LEFTSHIFTKEY]
space_key = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.SPACEKEY]

#tweak player
walkSpeed = 1.5
runSpeed = 2.5
turnSpeed = 2

#walk controls:
#left turn
if a_key and not shift_key:
    own.localAngularVelocity.z = turnSpeed - 1
    armature["aState"] = 5
if a_key and shift_key:
    own.localAngularVelocity.z = turnSpeed
    armature["aState"] = 5
#right turn
if d_key and not shift_key:
    own.localAngularVelocity.z = -turnSpeed + 1
    armature["aState"] = 6
if d_key and shift_key:
    own.localAngularVelocity.z = -turnSpeed
    armature["aState"] = 6
#forward
if w_key and not shift_key:
    own.localLinearVelocity.y = -walkSpeed
    armature["aState"] = 1
if w_key and shift_key and not own["stamina"] > 1:
    own.localLinearVelocity.y = -walkSpeed
    armature["aState"] = 1
if w_key and shift_key and own["stamina"] > 1:
    own.localLinearVelocity.y = -runSpeed
    own["stamina"] -= 2
    armature["aState"] = 2
#backward
if s_key and not shift_key:
    own.localLinearVelocity.y = walkSpeed - 0.6
    armature["aState"] = 3
if s_key and shift_key and not own["stamina"] > 1:
    own.localLinearVelocity.y = walkSpeed - 0.6
    armature["aState"] = 3
if s_key and shift_key and own["stamina"] > 1:
    own.localLinearVelocity.y = runSpeed - 1.4
    own["stamina"] -= 2
    armature["aState"] = 4
#animation to idle:
if not w_key and not a_key and not s_key and not d_key:
    if own["stamina"] > 100:
        armature["aState"] = 0
    else:
        armature["aState"] = 7
    
#restore stamina
if own["stamina"] < 1000:
    own["stamina"] += 1
if own["stamina"] < 2 and shift_key:
    if w_key or s_key:
        own["stamina"] = -50
        
#collecting
hitObj = ray.hitObject

#set globalDict values
bge.logic.globalDict["health"] = own["health"]
bge.logic.globalDict["stamina"] = own["stamina"]
bge.logic.globalDict["key1"] = own["key1"]

#collect key
if hitObj == obj["key1bound"]:
    own["key1"] = 1
    hitObj.children[0].endObject()

#define doors
door1 = obj["door1"]

#open door if you have a key
if hitObj == obj["door1"]:
    if own["key1"] == 1:
        if space_key and door1["open"] == 0:
            hitObj["open"] = 1
        elif space_key and door1["open"] == 1:
            hitObj["open"] = 0
            
#animate door
if door1["open"] == 1:
    if door1["frame"] < 10:
        door1["frame"] += 1
elif door1["open"] == 0:
    if door1["frame"] > 0:
        door1["frame"] -= 1