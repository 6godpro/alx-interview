# **Lockboxes**

## [0. Lockboxes](./0-lockboxes.py)
You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

* Prototype: `def canUnlockAll(boxes)`
* `boxes` is a list of lists
* A key with the same number as a box opens that box
* You can assume all keys will be positive integers
    * There can be keys that do not have boxes
* The first box `boxes[0]` is unlocked
* Return `True` if all boxes can be opened, else return `False`


### An example to explain the problem.

```bash
>>> BOXES => [[1], [2], [3], [4], []]
```
A box in the context is represented by a list contained in the list of lists. So in this case, [1] is a box and same goes for [2], [3] and so on.

To unlock a box, we need a key. A key in this context is the index of the box. So to unlock `box[1]`, the key we need is 0. Similarly, to unlock `box[2]`, the key we need is 1.

The integers represent keys, so basically when we unlock `box[1]`, with `key 0`, we get the key 1. In the same fashion, when we unlock `box[4]` with `key 3` (because the index is the key), we get `key 4`.

#### A walk through to explain the above example.
```bash
>>> BOXES => [[1], [2], [3], [4], []]
>>> INDEX =>   0    1    2    3    4

# each index is mapped to a box
```

The first box is always unlocked i.e you will always be given key 0. Next, we use it to unlock `box[1]`, which gives us `key 1` and then we use it to unlock `box[2]`, which gives `key 2` and so on until we get `key 4` which is used to unlock the last box. Then we return True because all boxes have been unlocked.

#### More examples
```bash
>>> canUnlockAll = __import__('0-lockboxes').canUnlockAll
>>> boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
>>> print(canUnlockAll(boxes))
True

>>> boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
>>> print(canUnlockAll(boxes))
False
```
