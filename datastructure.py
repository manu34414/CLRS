class STACK:
	def __init__(self, initial = []):
		self.stacklist = initial
		if len(initial) == 0:
			self.top = -1
		else:
			self.top = len(initial) - 1

	def isEmpty(self):
		if self.top == -1:
			return True
		else:
			return False

	def push(self, x):
		self.top += 1
		self.stacklist.append(x)

	def pop(self):
		if self.isEmpty():
			print('UNDERFLOW')
		else:
			del self.stacklist[-1]
			self.top -= 1

class QUEUE:
	def __init__(self, size):
		self.queuelist = []
		self.head = 0
		self.tail = 0
		self.size = size

	def isEmpty(self):
		if self.head == self.tail:
			return True
		else:
			return False

	def enqueue(self, x):
		if self.tail == self.size - 1:
			print("Overflow!!")
		else:
			self.queuelist.append(x)
			self.tail += 1

	def dequeue(self):
		if self.tail == 0:
			print("Underflow!!")
		else:
			del self.queuelist[0]
			self.tail -= 1

class Node:
	def __init__(self, key = None, prev = None, next = None):
		self.prev = prev
		self.key = key
		self.next = next

	def __str__(self):
		return self.key

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, node_x):
		if self.head == None:
			self.head = node_x
		else:
			node_x.next = self.head
			node_x.next.prev = node_x
			self.head = node_x

	def search(self, key):
		x = self.head
		while x != None and x.key != key:
			x = x.next
		return x

	def delete(self, node_x):
		# when node is not head
		if node_x.prev != None:
			node_x.prev.next = node_x.next
		# when node is head
		else:
			self.head = node_x.next
		# when node is not the last element in the Linkedlist
		if node_x.next != None:
			node_x.next.prev = node_x.prev

class LinkedList_s:
	# Create a NIL node
	def __init__(self):
		self.NIL = Node()
		self.NIL.next = self.NIL
		self.NIL.prev = self.NIL

	def insert(self, node_x):
		node_x.next = self.NIL.next
		self.NIL.next.prev = node_x
		self.NIL.next = node_x
		node_x.prev = self.NIL

	def delete(self, node_x):
		node_x.prev.next = node_x.next
		node_x.next.prev = node_x.prev

	def search(self, k):
		x = self.NIL.next
		while x != self.NIL and x.key != k:
			x = x.next
		return x

	def __str__(self):
		s = ""
		x = self.NIL.next
		while x != self.NIL:
			s += x.key
			x = x.next
		return s

class sinLinkedList:
	def __init__(self):
		self.NIL = Node()
		self.NIL.next = self.NIL

	def insert(self, key):
		node_x = Node(key)
		node_x.next = self.NIL.next
		self.NIL.next = node_x

	def delete(self, key):
		# Different from double linked list, to delete the first node X with key,
		# we should traverse the list right from beginning, and
		# record the node that comes right before X, which take O(n).
		x = self.NIL.next
		prev_x = self.NIL
		while x != self.NIL and x.key != key:
			x = x.next
			prev_x = prev_x.next
		prev_x.next = x.next

	def search(self, key):
		x = self.NIL.next
		while x != self.NIL and x.key != key:
			x = x.next
		return x

	# iterative
	def reverse(self):
		last = self.NIL
		current = self.NIL.next

		while current != self.NIL:
			# nextnode is what the current points to
			nextnode = current.next
			# current points to the previous node
			current.next = last
			# replace last with current , current with nextcode
			last = current
			current = nextnode
		self.NIL.next = last

	def __str__(self):
		s = ""
		x = self.NIL.next
		while x != self.NIL:
			s += x.key
			x = x.next
		return s

class Stack_ll(sinLinkedList):
	def isEmpty(self):
		if self.NIL.next == self.NIL:
			return True
		else:
			return False

	def push(self, key):
		# create a new Node x, with x.key = key
		self.insert(key)

	def pop(self):
		if self.NIL.next != self.NIL:
			self.NIL.next = self.NIL.next.next
		else:
			print('UnderFlow!!')

class Queue_ll(Stack_ll):
	def __init__(self):
		sinLinkedList.__init__(self)
		self.Tail = self.NIL

	def enqueue(self, key):
		newnode = Node(key)
		self.Tail.next = newnode
		newnode.next = self.NIL
		self.Tail = newnode

	def dequeue(self):
		self.pop()

class BSTnode:
	def __init__(self, key = None):
		self.p = None
		self.l = None
		self.r = None
		self.lpass = 0
		self.rpass = 0
		self.printed = 0
		self.key = key

class BST:
	def __init__(self):
		self.root = None

	def treewalk(self, Nstart):
		if Nstart != None:
			self.treewalk(Nstart.l)
			print(Nstart.key)
			self.treewalk(Nstart.r)

	def search(self, kvalue, startroot):
		if kvalue > startroot.key:
			return self.search(kvalue, startroot.r)
		elif kvalue == startroot.key or startroot == None:
			return startroot
		else:
			return self.search(kvalue, startroot.l)

	def search2(self, kvalue):
		Ncursor = self.root
		while Ncursor != None and Ncursor.key != kvalue:
			if kvalue > Ncursor.key:
				Ncursor = Ncursor.r
			else:
				Ncursor = Ncursor.l
		return Ncursor

	def findmin(self, Nstart):
		while Nstart.l != None:
			Nstart = Nstart.l
		return Nstart

	def findmax(self, Nstart):
		while Nstart.r != None:
			Nstart = Nstart.r
		return Nstart

	def successor(self, Nstart):
		if Nstart.r != None:
			return self.findmin(Nstart)
		Nparent = Nstart.p
		while Nparent != None and Nparent.r == Nstart:
			Nstart = Nparent
			Nparent = Nparent.p
		return Nparent

	def insert(self, kvalue):
		Nnew = BSTnode(kvalue)
		if self.root == None:
			self.root = Nnew
		else:
			Ncursor = self.root
			while True:
				if kvalue >= Ncursor.key:
					if Ncursor.r == None:
						Ncursor.r = Nnew
						Nnew.p = Ncursor
						break
					else:
						Ncursor = Ncursor.r
				else:
					if Ncursor.l == None:
						Ncursor.l = Nnew
						Nnew.p = Ncursor
						break
					else:
						Ncursor = Ncursor.l

	def transplant(self, Norigin, Nsub):
		if Norigin.p == None:
			self.root = Nsub
		elif Norigin.p.l == Norigin:
			Norigin.p.l = Nsub
		else:
			Norigin.p.r = Nsub
		if Nsub != None:
			Nsub.p = Norigin.p

	def delete(self, kvalue):
		Ntarget = self.search2(kvalue)
		if Ntarget.l == None:
			self.transplant(Ntarget, Ntarget.r)
		elif Ntarget.r == None:
			self.transplant(Ntarget, Ntarget.l)
		else:
			Nsuccessor = self.findmin(Ntarget.r)
			if Nsuccessor.p != Ntarget:
				self.transplant(Nsuccessor, Nsuccessor.r)
				Nsuccessor.r = Ntarget.r
				Nsuccessor.r.p = Nsuccessor
			self.transplant(Ntarget, Nsuccessor)
			Nsuccessor.l = Ntarget.l
			Nsuccessor.l.p = Nsuccessor

	def check(self, Nstart):
		result = []
		while Nstart != None:
			if Nstart.lpass == 0 and Nstart.l != None:
				Nstart.lpass = 1
				Nstart = Nstart.l
				continue

			if Nstart.printed == 0:
				if len(result) > 0:
					if Nstart.key < result[-1]:
						return False
					else:
						result.append(Nstart.key)
						Nstart.printed = 1
				else:
					result.append(Nstart.key)
					Nstart.printed = 1

			if Nstart.rpass == 0 and Nstart.r != None:
				Nstart.rpass = 1
				Nstart = Nstart.r
				continue
			Nstart = Nstart.p

		return True

if __name__ == '__main__':

	sampleBST = BST()
	sampleBST.insert(18)
	sampleBST.insert(17)
	sampleBST.insert(20)
	sampleBST.insert(15)
	sampleBST.insert(6)
	sampleBST.insert(7)
	sampleBST.insert(13)
	sampleBST.insert(9)
	sampleBST.insert(3)
	sampleBST.insert(2)
	sampleBST.insert(4)
	print(sampleBST.check(sampleBST.root))