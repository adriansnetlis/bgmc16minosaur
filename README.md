# bgmc16minosaur
A BGMC16 project called Minosaur

Everyone can join this Blender Game Engine game development!:)

Tasks:

-Minosaur AI:
*Walk randomly around maze between multiple target points. Rests in them!
*Cast 7 rays to player: head, both hands, both legs, torso, an empty at the eng of torchlight which is positioned basing on ray so it marks where light hits(I haven't made yet).
*Eash ray gives visibility +1 if it doesn't hit anything else in it's way, except player bounds or, better, ignore player bounds and test if there is anything else between Minosaur eyes(from where rays cast) and it's target. If there is something between them, the visibility reduces by 1, so min visibility = 0, max = 7.
*If visibility => 4 the Minosaur attacks player(currently just moves at speed 1.75 by tracking player).
*If door between him and player, he stops for 1 second, opens door and continue attack!
