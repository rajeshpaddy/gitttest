import hashlib
import pickle
import json
import jsonpickle

class Block:
	def __init__(self,val,hash):
		self.value=val
		self.__PREV_HASH=hash
		self.__MY_HASH=0
	def getValue(self):
		return self.value
	def getHash(self):
		return hashlib.md5(str(self.__PREV_HASH).encode('UTF-8')+str(self.value).encode('UTF-8')).hexdigest()
	def closeBlock(self):
		if self.__MY_HASH ==0:
			self.__MY_HASH=self.getHash()
		return self

default_or_previous_hash = hash("rajesh")
blockchain=[]
try:
	with open('blockchain.data','rb') as filehandle:
		file = jsonpickle.decode(pickle.load(filehandle))
		filehandle.close()

	for item in file:
		block = Block(item['value'],item['_Block__PREV_HASH']).closeBlock()
		if item['_Block__MY_HASH']==block.getHash():
			print("Good Block with value:" + item['value'])
		else:
			block._Block__MY_HASH=item['_Block__MY_HASH']
			print("Hash value mis match - Bad block with new value:" + str(item['value']))
		blockchain.append(block)
except FileNotFoundError:
	print("No file")
	
print("--------------")
while True:
	
	val=input("Enter the transaction value:")
	if val=="exit":
		break
	block = Block(val,default_or_previous_hash).closeBlock()
	default_or_previous_hash = block._Block__MY_HASH
	blockchain.append(block)
	print ("--------------")

with open('blockchain.data','wb') as filehandle:
	pickle.dump(jsonpickle.encode(blockchain,unpicklable=False),filehandle)

with open('blockchain.json','w') as jsonfilehandle:
	json.dump(jsonpickle.encode(blockchain,unpicklable=False),jsonfilehandle,indent=4)

print(len(blockchain))

for block in blockchain:
	print("PREV HASH:" + str(block._Block__PREV_HASH))
	print ("MY_HASH:" + str(block._Block__MY_HASH))
	print ("Value:"+ str(block.getValue()))
