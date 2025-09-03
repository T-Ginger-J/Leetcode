class Solution
  def find_substring(s, words)
    return [] if s.empty? || words.empty?

    word_len = words[0].length
    total_len = word_len * words.length
    word_count = Hash.new(0)
    words.each { |w| word_count[w] += 1 }
    result = []

    (0..(s.length - total_len)).each do |i|
      seen = Hash.new(0)
      j = 0
      while j < total_len
        word = s[i + j, word_len]
        break unless word_count.key?(word)
        seen[word] += 1
        break if seen[word] > word_count[word]
        j += word_len
      end
      result << i if j == total_len
    end

    result
  end
end
