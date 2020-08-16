"""
Scrabble Hand
Given a list of scrabble tiles (as dictionaries), create a function that outputs the maximum possible score a player can achieve by summing up the total number of points for all the tiles in their hand. 
Each hand contains 7 scrabble tiles.

Here's an example hand:

[
  { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }
]
The player's maximum_score from playing all these tiles would be 1 + 5 + 10 + 8 + 2 + 1 + 1, or 28.
"""
def maximum_score(tile_hand):
    
    ln = (len(tile_hand))
    
    a = []
    b = []
    for i in range(ln):
            a.append(tile_hand[i].values())
    
    for i in range(ln):
        b.append(list((a)[i])[1])
    return (sum(b))
    
    
maximum_score([
  { "tile": "B", "score": 2 },
  { "tile": "V", "score": 4 },
  { "tile": "F", "score": 4 },
  { "tile": "U", "score": 1 },
  { "tile": "D", "score": 2 },
  { "tile": "O", "score": 1 },
  { "tile": "U", "score": 1 }
])    
