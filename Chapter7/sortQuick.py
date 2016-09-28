import random

class QuickSort:
    def __init__(self, input):
        self.array = input

    def printarray(self):
        print(self.array)

    def quicksort(self, p, r):
        if p < r:
            # Get the separating point q
            q = self.partition(p, r)
            # Partition the left subarray
            self.quicksort(p, q-1)
            # Partition the right subarray
            self.quicksort(q+1, r)

    def partition(self, p, r):
        """
        Time: O(n), n = r-p+1
        """
        # Set the last element in A as pivot
        x = self.array[r]
        # Initiation of i
        i = p - 1
        for j in xrange(p, r):
            if self.array[j] < x:
                i += 1
                # Exchange A[i] and A[j]
                tmp = self.array[i]
                self.array[i] = self.array[j]
                self.array[j] = tmp
                # print(p, i, j, r)
                # print(self.array)

        # Exchange A[i+1] with A[r]
        # A[i+1] is the leftmost element that is larger than x
        tmp = self.array[i+1]
        self.array[i+1] = self.array[r]
        self.array[r] = tmp

        # i + 1 is the separating point q
        return i+1

    def randomizedPartition(self, p, r):
        # Generate the random number in range [p,r]
        i = random.randrange(p, r+1)

        # Exchange A[i] and A[r], A[i] is the pivot now
        tmp = self.array[i]
        self.array[i] = self.array[r]
        self.array[r] = tmp

        return self.partition(p, r)

    def randomizedQuicksort(self, p, r):
        if p < r:
            # Get the separating point q
            q = randomizedPartition(p, r)
            # sort the left subarray
            randomizedQuicksort(p, q-1)
            # sort the right subarray
            randomizedQuicksort(q+1, r)

if __name__ == '__main__':
    listarray = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    QS = QuickSort(listarray)
    QS.printarray()
    QS.quicksort(0, len(listarray)-1)
    QS.printarray()
