with open("file4.txt", "w") as f:
  t = f.write("Tahmid Hasan 67")
  t = f.truncate(6)  # it will store only 6 values
with open("file4.txt", "r") as f:
  t = f.read()
  print(t)