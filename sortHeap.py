class Heap:
    def __init__(self, input):
        self.array = input

    def printarray(self):
        print(self.array[1:])

    def maxheapify(self, k):
        """
        Function: Maintain the max-heap property, starting from the node whose
                  index is k
        Time: O(lg(n)) = O(h), where h is the height of the heap
        """
        heapsize = len(self.array) - 1
        left = 2 * k
        right = 2 * k + 1

        # the largeIndex is set as k by default
        largeIndex = k
        # Step1: Compare with left child
        if left < heapsize:
            if self.array[k] < self.array[left]:
                largeIndex = left

        # Step2: Compare with right child
        if right < heapsize:
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
        heapsize = len(self.array) - 1

        while k <= heapsize:
            left = 2 * k
            right = 2 * k + 1
            largeIndex = k

            if left <= heapsize:
                if self.array[k] < self.array[left]:
                    largeIndex = left

            if right <= heapsize:
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
        """
        Time: O(n)
        """
        # Starting from the last non-leave node
        heapsize = len(self.array) - 1
        start = int(heapsize/2)

        # Do the maxheapify for all non-leave nodes in a bottom-up way
        for i in range(start, 0, -1):
            self.maxheapify(i)

    def sortHeap(self):
        """
        Time: O(nlg(n))
        """
        self.buildmaxheap()
        fulllength = len(self.array)
        sorted = []
        for i in range(fulllength-1, 0, -1):
            # Exchange A[1] and A[i]
            tmp = self.array[1]
            self.array[1] = self.array[i]
            self.array[i] = tmp

            sorted.append(tmp)
            self.array = self.array[:-1]

            # Do the maxheapify in a top-down way
            self.maxheapify(1)
        return sorted

    def heapmaximum(self):
        # The first element in the array is the largest one, just return it
        return self.array[1]

    def heapextractmax(self):
        """
        After the heap is built, the first element in the heap must be the
        largest one.
        Step 1: Extract the A[1], which is the maximum element
        Step 2: Replace A[1] with last element A[-1]
        Step 3: Reduce the length of A by 1
        Step 4: Run the maxheapify to maintain max heap property
        Time: O(lg(n))
        """
        if len(self.array) <= 1:
            return 'Heap underflow'
        else:
            # Step 1: Extract the A[1], which is the maximum element
            max = self.array[1]
            # Step 2: Replace A[1] with last element A[-1]
            self.array[1] = self.array[-1]
            # Step 3: Reduce the length of A by 1
            del self.array[-1]
            # Step 4: Run the maxheapify to maintain max heap property
            self.maxheapify(1)
            return max

    def increasekey(self, k, key):
        """
        Time: O(lg(n))
        """
        if key < self.array[k]:
            print "New key is smaller than current key"
            return

        self.array[k] = key

        # Compare the key with the Parent
        while k > 1 and self.array[int(k/2)] < key:
            # if the key is larger than Parent, exchange A[i] and A[Parent[i]]
            self.array[k] = self.array[int(k/2)]
            k = int(k/2)
            self.array[k] = key

    def heapinsert(self, key):
        """
        Time: O(lg(n))
        """
        # Add the -inf as the last element in the array
        self.array.append(float("-inf"))
        k = len(self.array)-1
        # Increase the value of last element to key
        self.increasekey(k, key)

    def heapdelete(self, k):
        """
        Time: O(lg(n))
        """
        self.array[k] = self.array[-1]
        del self.array[-1]
        maxheapify(A, k)

if __name__ == '__main__':
    B = [5,13,2,25,7,17,20,8,4]
    updateB = [0] + B
    heapB = Heap(updateB)
    heapB.printarray()
    maxheapB = heapB.buildmaxheap()
    heapB.printarray()
    heapB.heapinsert(30)
    heapB.printarray()

    # heapB.increasekey(3,40)
    # heapB.printarray()
    # heapB.heapinsert(70)
    # heapB.printarray()
    # sorted = heapB.sortHeap()
    # print(sorted)

    # # sort B
    # print(sortHeap(updateB))
    # # build a maxheap
    # buildmaxheap(updateB)
    # print(updateB)
    # # return maximum
    # print(heapmaximum(updateB))
    # # extract max
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
