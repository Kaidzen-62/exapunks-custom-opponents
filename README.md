# Custom Opponents for EXAPUNKS

### Usage
Run the Python script from a terminal to create your opponent. Example:

  ```$ python3 custom_opponent.py battle-1.solution PB014 "UNNAMED0.PRJ" 2 ALPHA.exa BETA.exa```

Parameter names for a function:

```[output file name] [file name] [solution name] [number of programs] [names of program files]```

Place the resulting file in the opponents folder (Steam/steamapps/common/EXAPUNKS/Content/opponents).


#### Your resulting files should be named "battle-X.solution".

Where X is a number from 1 to 5. They correspond to five different levels in the game.

1 - KGOG-TV

2 - VALHALLA

3 - DEADLOCK'S DOMAIN

4 - THE WORMHOLE

5 - ABERDEEN


#### Where PB014 is a parameter unknown to me. They are special. If you change them to something else, the game will crash. I have no idea why. If I understand correctly, then this parameter is something like a file version. And this parameter is different for each level:

solution_number level_name parameter

1 - KGOG-TV - PB014

2 - VALHALLA - PB027

3 - DEADLOCK'S DOMAIN - PB022

4 - THE WORMHOLE - PB019

5 - ABERDEEN - PB031

And one last thing. 

Write code for NPCs as if it were the player's decision. For example, on the first level, my NPC's code has a GRAB 210 instruction, but it will actually take file 310.

That's all and have fun.
