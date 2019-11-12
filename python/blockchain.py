import hashlib
import pickle
import json
import jsonpickle

class Block:
	def __init__(self,val,hash):
		self.value=val
		self.PREV_HASH=hash
	def getValue(self):
		return self.value
	PREV_HASH=0
	def getHash(self):
		return hashlib.md5(str(self.PREV_HASH).encode('UTF-8')+str(self.value).encode('UTF-8')).hexdigest()
	MY_HASH=0
	def closeBlock(self):
		if self.MY_HASH ==0:
			self.MY_HASH=self.getHash()
		return self

default_or_previous_hash = hash("rajesh")
blockchain=[]
try:
	with open('blockchain.data','rb') as filehandle:
		file = jsonpickle.decode(pickle.load(filehandle))
		filehandle.close()

	for item in file:
		block = Block(item['value'],item['PREV_HASH']).closeBlock()
		if item['MY_HASH']==block.MY_HASH :
			print("Good Block with value:" + item['value'])
		else:
			block.MY_HASH=item['MY_HASH']
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
	default_or_previous_hash = block.MY_HASH
	blockchain.append(block)
	print ("--------------")

with open('blockchain.data','wb') as filehandle:
	pickle.dump(jsonpickle.encode(blockchain,unpicklable=False),filehandle)

print(len(blockchain))

for block in blockchain:
	print("PREV HASH:" + str(block.PREV_HASH))
	print ("MY_HASH:" + str(block.MY_HASH))
	print ("Value:"+ str(block.getValue()))
