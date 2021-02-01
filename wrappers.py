def wrap_brackets( text ):
  return "(" + text + ")"

def sq_brackets( text1):
    return "[[["+ text1 +"]]]"

def alt_brackets( text2):
    return "<<<"+ text2 +">>>"


text1=text=wrap_brackets("123456")
text2=text1=text


print( alt_brackets(sq_brackets(text1)))

