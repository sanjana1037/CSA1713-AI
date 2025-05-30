% Base case
sum_upto(1, 1).

% Recursive case
sum_upto(N, Sum) :-
    N > 1,
    N1 is N - 1,
    sum_upto(N1, Sum1),
    Sum is Sum1 + N.
