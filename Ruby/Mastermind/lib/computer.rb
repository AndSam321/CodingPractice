class Computer
  attr_reader :name, :guess
  
  def initialize(name = "Computer")
    @name = name
    @guess = nil
    @available_colors = %w[red green blue yellow orange purple]
  end
  
  def make_guess
    @guess = Array.new(4) { @available_colors.sample }
    puts "#{@name} guesses: #{@guess.join(' ')}"
    return @guess
  end
end