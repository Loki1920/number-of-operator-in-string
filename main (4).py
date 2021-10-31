s = str(input())
count=0
if '+' in s:
  count += 1
if '-' in s:
  count += 1
if '*' in s:
  count += 1
if '/' in s:
  count += 1
if '%' in s:
  count += 1
if '<' in s:
  count += 1
print(count)
  