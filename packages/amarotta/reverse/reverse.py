def reverse(args):

  inp = args.get("input")

  out = "Please provide a string"

  if inp != "":
    out = inp[::-1]

  return { "output": out }
