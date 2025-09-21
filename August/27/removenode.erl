%% Linked list as a tuple {Val, Next}, or [] for empty
-module(remove_nth).
-export([remove_nth_from_end/2, build_list/1, print_list/1]).

%% Build a linked list from a normal list
build_list([]) -> [];
build_list([H|T]) -> {H, build_list(T)}.

%% Print linked list
print_list([]) -> io:format("~n");
print_list({Val, Next}) ->
    io:format("~p ", [Val]),
    print_list(Next).

%% Main function
remove_nth_from_end(Head, N) ->
    {_NewHead, _Len, Result} = helper(Head, N),
    Result.

%% Helper: returns {current node, length, rebuilt list}
helper([], _N) -> {[], 0, []};
helper({Val, Next}, N) ->
    {_, Len, Rebuilt} = helper(Next, N),
    CurrLen = Len + 1,
    case CurrLen =:= N of
        true -> {Val, Next, Rebuilt};       %% skip this node
        false -> {Val, Next, {Val, Rebuilt}}
    end.
