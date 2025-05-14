def bubble_sort(array)
  length = array.length

  for i in 0...length
    swapped = false
    for j in 0...(length - i - 1)
      if array[j] > array[j + 1]
        array[j], array[j + 1] = array[j + 1], array[j]
        swapped = true
      end
    end
    if swapped == false
      break
    end
  end
  return array
end

p bubble_sort([4,3,78,2,0,2])

