defmodule MergeIntervals do
  def merge(intervals) do
    intervals
    |> Enum.sort_by(&elem(&1, 0))
    |> Enum.reduce([], fn {s, e}, acc ->
      case acc do
        [{ls, le} | rest] when s <= le -> [{ls, max(le, e)} | rest]
        _ -> [{s, e} | acc]
      end
    end)
    |> Enum.reverse()
  end

  # ---- Example Uses ----
  def demo do
    IO.inspect merge([{1, 3}, {2, 6}, {8, 10}, {15, 18}])
    IO.inspect merge([{1, 4}, {4, 5}])
    IO.inspect merge([{1, 2}, {3, 4}, {5, 6}])
    IO.inspect merge([{1, 10}, {2, 3}, {4, 5}, {6, 7}])
  end
end
