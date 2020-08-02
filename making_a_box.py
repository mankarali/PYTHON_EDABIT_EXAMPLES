"""
Making a Box
Create a function that creates a box based on dimension n.

Examples
make_box(5) ➞ [
  "#####",
  "#   #",
  "#   #",
  "#   #",
  "#####"
]

make_box(3) ➞ [
  "###",
  "# #",
  "###"
]

make_box(2) ➞ [
  "##",
  "##"
]

make_box(1) ➞ [
  "#"
]

"""

def make_box(n):
    return ['#' * n if i == 1 or i == n else '#' + ' ' * (n-2) + '#' for i in range(1,n+1)]



