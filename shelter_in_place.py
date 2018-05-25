import sys


def main():
    # Building Board
    board = dict()
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for i in letters:
        board[i] = dict()
        for j in range(10):
            board[i][j+1] = dict()

    # Input data
    food = [['A', 6], ['E', 9], ['I', 9]]
    water = [['F', 6], ['G', 9], ['H', 3]]
    wood = [['B', 10], ['E', 1], ['I', 4]]
    unavail = [['A', 10], ['A', 8], ['A', 5], ['A', 1],
               ['F', 1],
               ['G', 1], ['G', 10],
               ['J', 1], ['J', 2], ['J', 6], ['J', 7], ['J', 10]]

    # Unfortunately some resources require multiple trips per day to meet your needs.
    # Water requires three trips per day.
    # Firewood requires two trips per day,
    # and food requires one trip per day.
    # You must always return back to camp after visiting any resource location.
    trip_food, trip_water, trip_wood = 1, 3, 2

    # Best location object
    best_location = ['K', 0, sys.maxsize]

    # calculating distance
    for i in letters:
        for j in range(1, 11):
            location = [i, j]
            if location not in unavail:
                d_food, d_wood, d_water = sys.maxsize, sys.maxsize, sys.maxsize
                for k in food:
                    d_food = min(d_food, dist(location, k))
                for k in water:
                    d_water = min(d_water, dist(location, k))
                for k in wood:
                    d_wood = min(d_wood, dist(location, k))
                board[i][j]['food'] = d_food
                board[i][j]['water'] = d_water
                board[i][j]['wood'] = d_wood
                board[i][j]['total'] = (trip_food * d_food + trip_water * d_water + trip_wood * d_wood) * 2
                if board[i][j]['total'] < best_location[2]:
                    best_location = [i, j, board[i][j]['total']]

    print(best_location)
    print(board[best_location[0]][best_location[1]])


def dist(loc1, loc2):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    x1, y1 = loc1[0], loc1[1]
    x2, y2 = loc2[0], loc2[1]
    d_y = abs(y1 - y2)
    d_x = abs(letters.index(x1) - letters.index(x2))
    d = pow(pow(d_y, 2.0) + pow(d_x, 2.0), 0.5)
    return d


if __name__ == '__main__':
    main()
