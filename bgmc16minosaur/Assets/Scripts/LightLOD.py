#This script is made by cotax
#cotax is blenderartists.org user's nickname.

#1. Place a lamp in the scene and put its energy to 0.0

#2. Connect this script to the lamp, always(true)- python
    #- Add a property: energy(float) to the lamp
    #- Add a property: distance(integer) to the lamp


#Set the energy and distance to your likings


from bge import logic


own = logic.getCurrentController().owner
cam = own.scene.active_camera


#get the distance and energy from the light
distance = own['distance']
energy = own['energy']


#check distance and set the energy
if own.getDistanceTo(cam) < distance:
    own.energy = energy
else:
    own.energy = 0.0