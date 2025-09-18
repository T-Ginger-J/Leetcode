-module(merge_intervals).
-export([merge/1, demo/0]).

merge(Intervals) ->
    Sorted = lists:sort(fun({A,_},{B,_}) -> A < B end, Intervals),
    merge_sorted(Sorted, []).

merge_sorted([], Acc) -> lists:reverse(Acc);
merge_sorted([{S,E}|Rest], []) -> merge_sorted(Rest, [{S,E}]);
merge_sorted([{S,E}|Rest], [{LS,LE}|AccTail]) ->
    case S =< LE of
        true  -> merge_sorted(Rest, [{LS, max(LE,E)}|AccTail]);
        false -> merge_sorted(Rest, [{S,E},{LS,LE}|AccTail])
    end.

