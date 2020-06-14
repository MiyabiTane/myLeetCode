def readNumber(line, index):
  number = 0
  while index < len(line) and line[index].isdigit():
    number = number * 10 + int(line[index])
    index += 1
  if index < len(line) and line[index] == '.':
    index += 1
    keta = 0.1
    while index < len(line) and line[index].isdigit():
      number += int(line[index]) * keta
      keta /= 10
      index += 1
  token = {'type': 'NUMBER', 'number': number}
  return token, index


def readPlus(line, index):
  token = {'type': 'PLUS'}
  return token, index + 1


def readMinus(line, index):
  token = {'type': 'MINUS'}
  return token, index + 1


def readMalti(line, index):
  token = {'type': 'MALTI'}
  return token, index + 1


def readDevis(line, index):
  token = {'type': 'DEVIS'}
  return token, index + 1


def readLeft(line, index):
  token = {'type': 'LEFT'}
  return token, index + 1


def readRight(line, index):
  token = {'type': 'RIGHT'}
  return token, index + 1


def tokenize(line):
  line = line.replace(' ', '')
  tokens = []
  index = 0
  while index < len(line):
    if line[index].isdigit():
      (token, index) = readNumber(line, index)
    elif line[index] == '+':
      (token, index) = readPlus(line, index)
    elif line[index] == '-':
      (token, index) = readMinus(line, index)
    elif line[index] == '*':
      (token, index) = readMalti(line, index)
    elif line[index] == '/':
      (token, index) = readDevis(line, index)
    elif line[index] == '(':
      (token, index) = readLeft(line, index)
    elif line[index] == ')':
      (token, index) = readRight(line, index)
    elif line[index] == '.':
      line = line[:index] + '0' + line[index:]
      (token, index) = readNumber(line, index)
      
    # ALEXNOTE:  Doesn't it make sense to turn  '('  and ')' into Tokens?
    #            I think that would imporove code clarity.  It's also a more
    #            standard procedure for parsers.
    else:
      print('Invalid character found: ' + line[index])
      exit(1)
    tokens.append(token)
  #print(tokens)
  return tokens


def firstEvaluate(tokens):
  """
  evaluate 'MALTI' and 'DEVIS'

  input : tokens[dict] 
    dict['type'] = 'NUMBER,'PLUS','MINUS','MALTI','DEVIS'
  output : new_tokens[dict] 
    dict['type'] = 'NUMBER','PLUS','MINUS'
  """

  def checker(tokens, index):
    if tokens[index - 1]['type'] != 'NUMBER' or tokens[index + 1]['type'] != 'NUMBER':
        print('Invalid syntax')
        exit(1)

  tokens.insert(0, {'type': 'PLUS'})  # Insert a dummy '+' token
  index = 0
  while index < len(tokens):
    if tokens[index]['type'] == 'MALTI':
      checker(tokens, index)
      new_number = tokens.pop(index - 1)['number'] * tokens.pop(index)['number']
      tokens.insert(index - 1, {'type': 'NUMBER', 'number': new_number})
      tokens.pop(index)
    elif tokens[index]['type'] == 'DEVIS':
      checker(tokens, index)
      if tokens[index + 1]['number'] == 0:
        print("cannot devide by 0")
        exit(1)
      new_number = tokens.pop(index - 1)['number'] / tokens.pop(index)['number']
      tokens.insert(index - 1, {'type': 'NUMBER', 'number': new_number})
      tokens.pop(index)
    else:
      index += 1

  #print(tokens)
  return tokens


def secondEvaluate(new_tokens):
  """
  evaluate 'PLUS' and 'MINUS'

  input : new_tokens[dict] 
    dict['type'] = 'NUMBER','PLUS','MINUS'
  output : answer[float or int]
  """
  answer = 0
  index = 1
  while index < len(new_tokens):
    if new_tokens[index]['type'] == 'PLUS' or new_tokens[index]['type'] == 'MINUS':
      if new_tokens[index+1]['type'] != 'NUMBER':
        print("Invalid syntax")
        exit(1)
    if new_tokens[index]['type'] == 'NUMBER':
      if new_tokens[index - 1]['type'] == 'PLUS':
        answer += new_tokens[index]['number']
      elif new_tokens[index - 1]['type'] == 'MINUS':
        answer -= new_tokens[index]['number']
      else:
        print('Invalid syntax')
        exit(1)
    index += 1
  return answer


def tokenToNumber(tokens):
  new_tokens = firstEvaluate(tokens)
  actualAnswer = secondEvaluate(new_tokens)
  return actualAnswer


def evaluate(tokens):
  """
  input : line[str]
    list[0] = '(' and list[-1] = ')'
  output : num [int]
  """
  stack = []
  index = 0
  # ALEXNOTE: this logic can be simpler if you use tokens for ( and ).
  #           I do think it's good to use stack to avoid recursion, though.
  
  # ALEXNOTE - one more time -  Very nice !  using tokens for the parenthesis makes it clearer to read!
  while index < len(tokens):
    if tokens[index]['type'] == 'LEFT':
      stack.append(['LEFT', index])
      index += 1
    elif tokens[index]['type'] == 'RIGHT':
      if not stack[-1][0] == 'LEFT':
        print('invalid syntax')
        exit(1)
      left_index = stack.pop()[1]
      number = tokenToNumber(tokens[left_index + 1: index])
      tokens = tokens[: left_index] + tokens[index + 1:]
      tokens.insert(left_index, {'type': 'NUMBER', 'number': number}) 
      index = left_index + 1
    else:
      index += 1
  if not stack:
    number = tokenToNumber(tokens)
    return number
  else:
    print("invalid syntax")
    exit(1)
  


def test(line):
  if len(line) == 0:
    print("please input some numbers")
    return None
  tokens = tokenize(line)
  actualAnswer = evaluate(tokens)
  expectedAnswer = eval(line)
  if abs(actualAnswer - expectedAnswer) < 1e-8:
    print("PASS! (%s = %f)" % (line, expectedAnswer))
  else:
    print("FAIL! (%s should be %f but was %f)" %
          (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
  print("==== Test started! ====")
  #test("")
  test("1")
  test("1+2")
  test("12+3")
  test("1.0+2")
  test("1-3")
  test("2.0-13")
  test("3-14+4.0")
  test("2*3")
  test("4.2*9")
  test("2*2*2")
  test("3*5.9+2")
  test("6.0-4*2")
  test("8/9")
  test("6/3.0/4")
  test("6.0/4")
  test("4*5-7.0/3+2")
  test("3+2+4.0*4-4/2.0")
  test("(2)")
  test("(2+3)*2")
  test("2.3*(3-1)")
  test("((2.3+4)+5)*4")
  # ALEXNOTE: good test - parenthesis within parenthesis
  test("3/(2+3)*4")
  test("5+2*6.3/(3-0.2+1*4)+3.2")
  #test("(3/((4-2))")
  #test("3/0")
  test("(2+.04)*3/(3+4.5)")
  print("==== Test finished! ====\n")


runTest()


while True:
  print('> ', end="")
  line = input()
  tokens = tokenize(line)
  actualAnswer = evaluate(tokens)
  answer = eval(line)
  print("answer = %f\n" % answer)

