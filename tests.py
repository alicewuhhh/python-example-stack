from Stack import Stack

def test_empty():
	s = Stack()
	assert s.isEmpty()
	assert s.size() == 0

def test_it():
	s = Stack()
	s.push(1)
 	assert s.size() ==1
	
# 	assert s.size == 0

# 	for i in range(1):
#   		s.push(i)
# 	assert s.size() = 101
# 	raise NotImplementedError('Need to implement a simple test.')
