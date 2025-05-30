state(middle, onbox, middle, hasnot).
move(state(middle, onbox, middle, hasnot), grasp, state(middle, onbox, middle, has)).
can_get(State) :- move(State, grasp, _).
QUERY: can_get(state(middle, onbox, middle, hasnot)).
