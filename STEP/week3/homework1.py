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
  token = {'type' : 'MALTI'}
  return token, index + 1


def readDevis(line, index):
  token = {'type' : 'DEVIS'}
  return token, index + 1


def tokenize(line):
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
    else:
      print('Invalid character found: ' + line[index])
      exit(1)
    tokens.append(token)
  #print(tokens)
  return tokens


def first_evaluate(tokens):

  def checker():
    if not tokens[index]['type'] == 'NUMBER':
        print("your input is not good")
        exit(1)

  new_tokens = [{'type': 'PLUS'}]  # Insert a dummy '+' token
  index = 0
  while index < len(tokens):
    if tokens[index]['type'] == 'NUMBER':
      sub_number = tokens[index]['number']
      if tokens[min(index + 1, len(tokens) - 1)]['type'] == 'MALTI':
        index += 2
        checker()
        sub_number *= tokens[index]['number']
        new_tokens.append({'type': 'NUMBER', 'number': sub_number})
      elif tokens[min(index + 1, len(tokens) - 1)]['type'] == 'DEVIS':
        index += 2
        checker()
        if not tokens[index]['number'] == 0:
          sub_number /= tokens[index]['number'] 
        else:
          print("you cannot devide by 0")
          exit()
        new_tokens.append({'type': 'NUMBER', 'number': sub_number})
      else:
        new_tokens.append(tokens[index])
    else:
      new_tokens.append(tokens[index])
    index += 1
  #print(new_tokens)
  return new_tokens


def second_evaluate(new_tokens):
  answer = 0
  index = 1
  while index < len(new_tokens):
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


def test(line):
  if len(line) == 0:
    print("please input some numbers")
    return None
  tokens = tokenize(line)
  new_tokens = first_evaluate(tokens)
  actualAnswer = second_evaluate(new_tokens)
  expectedAnswer = eval(line)
  if abs(actualAnswer - expectedAnswer) < 1e-8:
    print("PASS! (%s = %f)" % (line, expectedAnswer))
  else:
    print("FAIL! (%s should be %f but was %f)" %
          (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
  print("==== Test started! ====")
  test("")
  test("1")
  test("1+2")
  test("12+3")
  test("1.0+2")
  test("1-3")
  test("2.0-13")
  test("3-14+4.0")
  test("2*3")
  test("4.2*9")
  test("3*5.9+2")
  test("6.0-4*2")
  test("8/9")
  test("6.0/4")
  test("4*5-7.0/3+2")
  test("3/0")
  test("3+2+4.0*4-4/2.0")
  print("==== Test finished! ====\n")


runTest()

"""
while True:
  print('> ', end="")
  line = input()
  tokens = tokenize(line)
  new_tokens = first_evaluate(tokens)
  answer = second_evaluate(new_tokens)
  print("answer = %f\n" % answer)
"""
