students = ["Draco Malfoy", "Vincent Crabbe", "Gregory Goyle", "Millicent Bulstrode"]

def circle_turns(students: list, max: int):
  num_students = len(students)
  for i in range(max):
    yield students[i % num_students]

cleanup_turns = circle_turns(students, 12)

for name in cleanup_turns:
  print(f"{name}, it's your turn to cleanup Slytherin's common room!")
