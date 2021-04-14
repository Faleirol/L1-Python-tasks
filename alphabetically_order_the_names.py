Chocolate_Bars = 18
People = 5
Whole_bars = Chocolate_Bars // People
Extra_squares = Whole_bars % 7
squares_leftover = Whole_bars * 7 % People
print("Whole_bars:{}".format(Whole_bars))
print("Extra_squares:{}".format(Extra_squares))
print("Squares_leftover:{}".format(squares_leftover))
