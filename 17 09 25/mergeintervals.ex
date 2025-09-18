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

