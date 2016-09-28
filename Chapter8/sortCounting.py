class CountSort:
    def __init__(self, input):
        self.array = input

    def printarray(self):
        print(self.array)

    def countsort(self, kvalue):
        """
        kvalue is the maximum value of A, which is to say, all elements in A is
        within the range of [0, kvalue]
        """
        length = len(self.array)
        # B records the sorted array, C record the number of appearance
        B, C = [0] * (length+1), [0] * (kvalue + 1)

        # C[i] contains the number of elements equal to i
        for j in self.array:
            C[j] += 1

        for i in xrange(1, len(C)):
            C[i] += C[i-1]

        # C[A[j]] is the right position of A[j] in the final sorted array
        for j in xrange(length-1, -1, -1):
            B[C[self.array[j]]] = self.array[j]
            C[self.array[j]] -= 1
        return B[1:]

if __name__ == '__main__':
    unsorted = [6,0,2,0,1,3,4,6,1,3,2]
    sorting = CountSort(unsorted)
    sorted = sorting.countsort(6)
    print(sorted)
