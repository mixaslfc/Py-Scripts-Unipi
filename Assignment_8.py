# Chess board 8*8/7*8/7*7 with a White Tower and a Black Bishop at random positions. 
# Every turn the player that can defeat the other takes 1 point.
# Print  the result table after 100 turns.

# Chess board
import random



def chessboard64(x):

    white_wins = 0
    black_wins = 0
    numbers=list(reversed(range(1,9)))
    digits=list('ABCDEFGH') 

    # Play the chess board with the white tower and the black bishop x times
    for i in range(x):

        # Create a chess board 8*8
        row=list(range(8))
        collumn=list(range(8))
        chessboard = [['##' for i in collumn] for j in row]
        
        # Put a white tower at random position
        wt_row=random.randint(0,7) 
        wt_collumn=random.randint(0,7)
        chessboard[wt_row][wt_collumn] = 'WT'

        # Put a black bishop at random position
        bb_row=random.randint(0,7)
        bb_collumn=random.randint(0,7)        
        # To avoid the white tower and the black bishop to be in the same position
        while wt_row == bb_row & wt_collumn == bb_collumn:
            bb_row=random.randint(0,7)
            bb_collumn=random.randint(0,7)        
        chessboard[bb_row][bb_collumn] = 'BB'
        
        # Comment code is for printing the chess board with the positions of the white tower and the black bishop            
        # for i in range(8):
        #     print ('  '+digits[i],end='')        
        # print() 
        # for i in range(8):
        #     print (numbers[i], end=" ")
        #     for j in range(8):
        #         print(chessboard[i][j], end=' ')
        #     print()

        # Check if the white tower can defeat the black bishop 
        if (wt_row == bb_row) or (wt_collumn == bb_collumn):
            # print("White wins!")
            white_wins += 1
        # Check if the black bishop can defeat the white tower
        elif (wt_row + wt_collumn == bb_row + bb_collumn) or (wt_row - wt_collumn == bb_row - bb_collumn):
            # print("Black wins!")
            black_wins += 1

    winners_table="White wins:"+str(white_wins)+"\nBlack wins:"+str(black_wins)        
    return winners_table          

def chessboard56(x):
    white_wins = 0
    black_wins = 0
    numbers=list(reversed(range(1,8)))
    digits=list('ABCDEFGH') 

    # Play the chess board with the white tower and the black bishop x times
    for i in range(x):

        # Create a chess board 7*8
        row=list(range(7))
        collumn=list(range(8))
        chessboard = [['##' for i in collumn] for j in row]
        
        # Put a white tower at random position
        wt_row=random.randint(0,6) 
        wt_collumn=random.randint(0,7)
        chessboard[wt_row][wt_collumn] = 'WT'

        # Put a black bishop at random position
        bb_row=random.randint(0,6)
        bb_collumn=random.randint(0,7)        
        # To avoid the white tower and the black bishop to be in the same position
        while wt_row == bb_row & wt_collumn == bb_collumn:
            bb_row=random.randint(0,6)
            bb_collumn=random.randint(0,7)        
        chessboard[bb_row][bb_collumn] = 'BB'
        
        # Comment code is for printing the chess board with the positions of the white tower and the black bishop            
        # for i in range(7):
        #     print ('  '+digits[i],end='')        
        # print() 
        # for i in range(7):
        #     print (numbers[i], end=" ")
        #     for j in range(8):
        #         print(chessboard[i][j], end=' ')
        #     print()

        # Check if the white tower can defeat the black bishop 
        if (wt_row == bb_row) or (wt_collumn == bb_collumn):
            # print("White wins!")
            white_wins += 1
        # Check if the black bishop can defeat the white tower
        elif (wt_row + wt_collumn == bb_row + bb_collumn) or (wt_row - wt_collumn == bb_row - bb_collumn):
            # print("Black wins!")
            black_wins += 1

    winners_table="White wins:"+str(white_wins)+"\nBlack wins:"+str(black_wins)        
    return winners_table  

def chessboard49(x):
    white_wins = 0
    black_wins = 0
    numbers=list(reversed(range(1,8)))
    digits=list('ABCDEFGH') 

    # Play the chess board with the white tower and the black bishop x times
    for i in range(x):

        # Create a chess board 7*7
        row=list(range(7))
        collumn=list(range(7))
        chessboard = [['##' for i in collumn] for j in row]
        
        # Put a white tower at random position
        wt_row=random.randint(0,6) 
        wt_collumn=random.randint(0,6)
        chessboard[wt_row][wt_collumn] = 'WT'

        # Put a black bishop at random position
        bb_row=random.randint(0,6)
        bb_collumn=random.randint(0,6)        
        # To avoid the white tower and the black bishop to be in the same position
        while wt_row == bb_row & wt_collumn == bb_collumn:
            bb_row=random.randint(0,6)
            bb_collumn=random.randint(0,6)        
        chessboard[bb_row][bb_collumn] = 'BB'
        
        # Comment code is for printing the chess board with the positions of the white tower and the black bishop            
        # for i in range(7):
        #     print ('  '+digits[i],end='')        
        # print() 
        # for i in range(7):
        #     print (numbers[i], end=" ")
        #     for j in range(7):
        #         print(chessboard[i][j], end=' ')
        #     print()

        # Check if the white tower can defeat the black bishop 
        if (wt_row == bb_row) or (wt_collumn == bb_collumn):
            # print("White wins!")
            white_wins += 1
        # Check if the black bishop can defeat the white tower
        elif (wt_row + wt_collumn == bb_row + bb_collumn) or (wt_row - wt_collumn == bb_row - bb_collumn):
            # print("Black wins!")
            black_wins += 1

    winners_table="White wins:"+str(white_wins)+"\nBlack wins:"+str(black_wins)        
    return winners_table

# Play the chess 8*8
print("--Result of chess 8*8--")
print(chessboard64(100))

# Play the chess 7*8
print("--Result of chess 7*8--")
print(chessboard56(100))

# Play the chess 7*7
print("--Result of chess 7*7--")
print(chessboard49(100))       
   