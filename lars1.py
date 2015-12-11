from mc import *
from turtle import *

mc = Minecraft()

t = new turtle()

mc.postToChat("Hello world!")

playerPos = mc.player.getPos()
mc.setBlock(playerPos.x,playerPos.y-1,playerPos.z,MUSHROOM_RED)

# length = 2*2*2*2
# mc.setBlocks(playerPos.x,playerPos.y,playerPos.z,
#             playerPos.x+length-1,playerPos.y+length-1,playerPos.z+length-1,MUSHROOM_RED)


t.penblock(GOLD_BLOCK)
t.go(50)
t.right(90)
t.go(50)
t.right(90)
t.go(50)
t.right(90)
t.go(50)
