hash_table_size = 8  # O(1)

hash_table = [None] * hash_table_size


def myhash(s):
	# NAIVE hashing function dont use IRL   output is 32 bit
	str_bytes = str(s).encode()
	total = 0
	for b in str_bytes:   # O(n)  Typical usage probably O(1) 
		total += b

	return total

def hash_index(s):
	h = myhash(s)
	return h % hash_table_size

def put(key,value):
	index = hash_index(key)
	hash_table[index] = value

def get(key):
	index = hash_index(key)
	return hash_table[index]

def delete(key):
	index = hash_index(key)
	hash_table[index] = None

	

if __name__ == "__main__":
	#  If running from command line
	print(hash_index("hello"))
	print(hash_index("jose"))
	print(hash_index("jeff"))
	print(hash_index("Beej"))
	print(hash_index("jeeb"))
	print(hash_index("jez"))



	# print(hash_table)
	# put("Hello" , 37)
	put("jose" , 337)
	put("jeff" , 237)
	put("beej" , 137)
	
	print(hash_table)
	print(get('hello'))
