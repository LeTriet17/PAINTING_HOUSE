def __main__():
    input_tiles = input("Enter the tile colors: ")
    res = (input_tiles + '.')[:-1]
    input_col = {}
    col = {'R', 'G', 'Y', 'B'}
    min_tiles = 0
    input_col = {c for c in input_tiles}
    remain_col = col - input_col
    for i in range(len(input_tiles) - 1):
        if len(input_tiles) and input_tiles[i] == input_tiles[i+1]:
            if (i + 2 < len(input_tiles)):
                replace_cols = {c for c in input_col if c !=
                               input_tiles[i] and c != input_tiles[i+2]}
            else:
                replace_cols = {c for c in input_col if c != input_tiles[i]}
            if len(replace_cols) == 0:
                replace_col = remain_col.pop()
                input_col.add(replace_col)
                replace_cols.add(replace_col)
            res = res[:i+1] + replace_cols.pop() + res[i+2:]
            input_tiles = res
            min_tiles += 1
    print(res, min_tiles)


__main__()
