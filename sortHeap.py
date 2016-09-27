class Heap:
	def __init__(self, input):
		self.array = input
		self.heapsize = len(self.array) - 1

	def printarray(self):
		print(self.array[1:])


	def maxheapify(self, k):
        """
        Function: Maintain the max-heap property, starting from the node whose
                  index is k
        Time: O(lg(n)) = O(h), where h is the height of the heap
        """
		left = 2 * k
		right = 2 * k + 1

		# Step1: Compare with left child
		if left <= self.heapsize:
			if self.array[k] < self.array[left]:
				largeIndex = left
			else:
				largeIndex = k

		# Step2: Compare with right child
		if right <= self.heapsize:
			if self.array[largeIndex] < self.array[right]:
				largeIndex = right

		if largeIndex != k:
			# Exchange A[k] with A[largeIndex]
			tmp = self.array[largeIndex]
			self.array[largeIndex] = self.array[k]
			self.array[k] = tmp

			self.maxheapify(largeIndex)

	# do the maxheapify in an iterative way
	def maxheapify_loop(self, k):
		while k <= self.heapsize:
			left = 2 * k
			right = 2 * k + 1

			if left <= self.heapsize:
				if self.array[k] < self.array[left]:
					largeIndex = left
				else:
					largeIndex = k

			if right <= self.heapsize:
				if self.array[k] < self.array[right]:
					largeIndex = right

			if largeIndex != k:
				tmp = self.array[largeIndex]
				self.array[largeIndex] = self.array[k]
				self.array[k] = tmp

				# just like self.maxheapfy(largeIndex) in recursive method
				k = largeIndex
			else:
				# if largeIndex == k, it means the max-heap property is satisfied
				# just break out the loop
				break

	def buildmaxheap(self):
		start = int(len(self.array)/2)
		for i in range(start, 0, -1):
			self.maxheapify(i)

	def heapdelete(self, k):
		self.array[k] = self.array[-1]
		del self.array[-1]
		maxheapify(A, k)

	def increasekey(self, k, key):
		self.array[k] = key
		while int(k/2) >= 1 and self.array[int(k/2)] < key:
			self.array[k] = self.array[int(k/2)]
			k = int(k/2)
		self.array[k] = key

	def heapinsert(self, key):
		self.array.append(key)
		k = len(self.array)-1
		while int(k/2) >= 1 and self.array[int(k/2)] < key:
			# swap A[parent] and key
			self.array[k] = self.array[int(k/2)]
			k = int(k/2)
		self.array[k] = key

	def heapmaximum(self):
		return self.array[1]

	def heapextractmax(self):
		if len(self.array) <= 1:
			return 'Heap Empty'
		else:
			max = self.array[1]
			self.array[1] = self.array[len(self.array)-1]
			del self.array[-1]
			self.maxheapify(1)
			return max

	def sortHeap(self):
		self.buildmaxheap()
		fulllength = len(self.array)
		sorted = []
		for i in range(fulllength-1, 1, -1):
			tmp = self.array[1]
			self.array[1] = self.array[i]
			self.array[i] = tmp
			sorted.append(tmp)
			self.array = self.array[:-1]
			self.maxheapify(1)
		return sorted


if __name__ == '__main__':
	B = [5,13,2,25,7,17,20,8,4]
	updateB = [0] + B
	heapB = Heap(updateB)
	heapB.printarray()
	heapB.buildmaxheap()
	heapB.printarray()
	heapB.increasekey(3,40)
	heapB.printarray()
	heapB.heapinsert(70)
	heapB.printarray()
	sorted = heapB.sortHeap()
	print(sorted)

	# # sort B
	# print(sortHeap(updateB))
	# # build a maxheap
	# buildmaxheap(updateB)
	# print(updateB)
	# # return maximum
	# print(heapmaximum(updateB))
	# # extract max
	# maxelem = heapextractmax(updateB)
	# print(updateB)
	# # insert key 40
	# heapinsert(updateB, 40)
	# print(updateB)
	# # increase key
	# increasekey(updateB, 4, 50)
	# print(updateB)
	# # delete key
	# heapdelete(updateB, 2)
	# print(updateB)
