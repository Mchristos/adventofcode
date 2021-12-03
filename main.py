import os
for i in range(31):
    path = f'day{i}.py'
    if os.path.exists(path):
        print(f"---- Day {i}  ----")
        exec(open(path).read())
        print("\n")