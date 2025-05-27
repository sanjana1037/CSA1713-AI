% --- Academic Database with Name and Date of Birth ---

% Facts: student(Name, DOB)
student('Alice', '12-03-2001').
student('Bob', '25-07-2000').
student('Charlie', '01-01-2002').
student('David', '19-11-2001').
student('Eva', '30-05-2003').

% Rule to display all students
display_all :-
    student(Name, DOB),
    format('Name: ~w, DOB: ~w~n', [Name, DOB]),
    fail.
display_all.
