def encript(string, shift)
  result = ""
  string.each_char do |char|
    if char.match?(/[a-zA-Z]/)
      if char.match?(/[A-Z]/)
        result += ((char.ord - 65 + shift) % 26 + 65).chr
      else
        result += ((char.ord - 97 + shift) % 26 + 97).chr
      end
    else
      result += char
    end  
  end
  return result
end

puts encript("What a string!", 5)