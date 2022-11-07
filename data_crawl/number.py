units_10k = [' ','만', '억', '조']

def getNumber(text):
  try:
    if text[-1] >= '0' and text[-1] <= '9' :
     num = int(text.replace(',',''))
    else :
     digit = 10000**(units_10k.index(text[-1]))
     num = int(float(text[:-1]) * digit)
  except:
    print(f'invalid Number Exception {text}')
  return num

# code for check getNumber
if __name__ == "__main__":
  list = ['9,249','783','1,180','1.8만','1.1만']
  for idx, txt in enumerate(list):
    list[idx] = getNumber(txt)
  list.sort()
  for num in list:
    print(num)
  