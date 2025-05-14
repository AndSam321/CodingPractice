class Player
  attr_accessor :name, :marker

  def initialize(name, marker)
    @name = name
    @marker = marker
  end

  def to_s
    "#{@name} (#{@marker})"
  end

  
end