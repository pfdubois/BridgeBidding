# python fixgloss.py to sort source/Glossary.rst into output.rst
L1=3

def blanks(line):
   n = 0
   for c in line:
       if c == '\n':
           return 0
       if c == '\t': raise ValueError(f"tab in %s"% line)
       if c.isalpha():
          return(n)
       else:
           n += 1
   return(n)
      
with open("source/Glossary.rst") as f:
   lines = f.readlines()

sawsorted = False
tstart = [1]
tend = [1]
sawterm = False
nline = 0
for line in lines:
   nline += 1
   if line.startswith("   :sorted"):
      sawsorted = True
   elif sawsorted:
      if blanks(line) == L1 :
         if sawterm:
            tend[-1] = nline
         else:
            sawterm = True
            tend[-1] = nline-1
            tstart.append(nline)
            tend.append(nline)
      else:
          sawterm = False
else:
   nline += 1
   tend[-1] = nline

dl = {}
for i in range(1, len(tstart)):
   key = lines[tstart[i]-1].strip()
   dl[key] = (tstart[i], tend[i])
#   print(key, type(tstart[i]),tstart[i], tend[i])

with open("output.txt", "w") as g:
   for line in lines[(tstart[0]-1): tend[0]]:
      g.write(line)
   keylist = sorted(dl.keys())
   for key in keylist:
      start, stop = dl[key]
      for line in lines[(start-1): stop]:
         g.write(line)

