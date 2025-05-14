def substrings(target, dictionary)
  result = Hash.new(0)
  
  for word in dictionary
    count = target.downcase.scan(word.downcase).length
    if count > 0 
      result[word] += count
    end
  end
  return result
end
  

puts substrings("Howdy partner, sit down! How's it going?", ["below","down","go","going","horn","how","howdy","it","i","low","own","part","partner","sit"])