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

%% ---- Example Uses ----
demo() ->
    io:format("~p~n", [merge([{1,3},{2,6},{8,10},{15,18}])]),
    io:format("~p~n", [merge([{1,4},{4,5}])]),
    io:format("~p~n", [merge([{1,2},{3,4},{5,6}])]),
    io:format("~p~n", [merge([{1,10},{2,3},{4,5},{6,7}])]).
