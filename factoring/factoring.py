from z3 import Int, Solver, sat


N = Int(13 * 17)

P = Int('P')
Q = Int('Q')

solver = Solver()

solver.add(P * Q == N)

if solver.check() == sat:
  model = solver.model()
  print(f'P: {model[P]} Q: {model[Q]}')
else:
  print("No solution found")