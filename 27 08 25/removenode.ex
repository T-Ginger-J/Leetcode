defmodule RemoveNth do
  # Build linked list as tuples {val, next}
  def build_list([]), do: nil
  def build_list([h | t]), do: {h, build_list(t)}

  # Print linked list
  def print_list(nil), do: IO.puts("")
  def print_list({val, next}) do
    IO.write("#{val} ")
    print_list(next)
  end

  # Main function: remove nth node from end
  def remove_nth_from_end(head, n) do
    {_len, new_head} = helper(head, n)
    new_head
  end

  # Helper: returns {length, rebuilt list}
  defp helper(nil, _n), do: {0, nil}
  defp helper({val, next}, n) do
    {len, rebuilt} = helper(next, n)
    curr_len = len + 1

    if curr_len == n do
      {curr_len, rebuilt}  # skip current node
    else
      {curr_len, {val, rebuilt}}
    end
  end
end

# Example Usage
head = RemoveNth.build_list([1, 2, 3, 4, 5])
new_head = RemoveNth.remove_nth_from_end(head, 2)
RemoveNth.print_list(new_head)  # Output: 1 2 3 5
