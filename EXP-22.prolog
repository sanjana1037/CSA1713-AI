% Facts: bird species and flight capability
bird(sparrow).
bird(eagle).
bird(penguin).
bird(ostrich).
bird(parrot).
bird(kiwi).

can_fly(sparrow).
can_fly(eagle).
can_fly(parrot).

% Rule: A bird can fly if it's in the list of flying birds
can_bird_fly(X) :- 
    bird(X), 
    can_fly(X).

% Rule: A bird cannot fly if it's a bird but not in the list of flying birds
cannot_bird_fly(X) :- 
    bird(X), 
    \+ can_fly(X).
