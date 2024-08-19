groceries = ['test', 'hello']
for item in groceries:
	print(item)

for index, item in enumerate(groceries, 1):
	print(f'{index}. {item}')

if 'hello' in "helloguy":
	#do something
	print('yes')
else:
	#do something else
	print('no')