class Board
  def initialize
    @board = Array.new(9, " ")
  end
  
  def display
    puts "#{@board[0]} | #{@board[1]} | #{@board[2]}"
    puts "---------"
    puts "#{@board[3]} | #{@board[4]} | #{@board[5]}"
    puts "---------"
    puts "#{@board[6]} | #{@board[7]} | #{@board[8]}"
  end

  def update(position, marker)
    @board[position] = marker
  end

  def reset
  @board = Array.new(9, " ")
  end

  def game_status
  winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], 
    [0, 3, 6], [1, 4, 7], [2, 5, 8], 
    [0, 4, 8], [2, 4, 6]            
  ]
  
  winning_combinations.each do |combo|
    if @board[combo[0]] == @board[combo[1]] && @board[combo[1]] == @board[combo[2]] && @board[combo[0]] != " "
      return @board[combo[0]] 
    end
  end
  if @board.include?(" ") == false
    return "The game is tied!"
  end
  return "continue"
  end
end
