

def getValues(**args):
  print(args)
  values = args.values()
  print(args.values())
  return args
  
x = getValues(a=1, b=2, c=3)

print(x["a"])

def manyParams():\
  return 1
