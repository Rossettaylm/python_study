news = [1,2,3,4,5,6,7]
print(news)
print("The length of news is "+str(len(news)))
print("The first three items in the list are:")
#切片
for new in news[:3]:
	print(new)
print("Three items from the middle of list are:")
for new in news[2:5]:
	print(new)
print("The last three items in the list are:")
for new in news[-3:]:
	print(new)
#通过切片复制列表
numbers = news[:]
print("\n" + str(numbers))
