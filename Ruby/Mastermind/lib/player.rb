class Player
  attr_reader :name, :guess
  
  def initialize(name)
    @name = name
    @guess = nil
  end
  
  def make_guess
    puts "#{@name}, enter your guess (4 colors separated by spaces):"
    puts "Available colors: red, green, blue, yellow, orange, purple"
    input = gets.chomp.downcase.split
    @guess = input
    return @guess
  end
end