def find_substring(s, words)
  return [] if s.empty? || words.empty?

  word_len = words[0].size
  word_count = words.size
  total_len = word_len * word_count
  word_map = Hash.new(0)
  words.each { |w| word_map[w] += 1 }
  res = []

  (0...word_len).each do |i| # start with each offset
    left = i
    seen = Hash.new(0)
    count = 0

    (i..s.size - word_len).step(word_len) do |j|
      word = s[j, word_len]

      if word_map.key?(word)
        seen[word] += 1
        count += 1

        while seen[word] > word_map[word]
          left_word = s[left, word_len]
          seen[left_word] -= 1
          left += word_len
          count -= 1
        end

        res << left if count == word_count
      else
        seen.clear
        count = 0
        left = j + word_len
      end
    end
  end

  res
end
