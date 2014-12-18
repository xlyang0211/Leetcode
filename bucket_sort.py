from math import floor

class Node:
    """Each node represent a data in the array. except the first one
    """
    def __init__(self):
        self.data = 0
        self.next = None

class BucketSort:
    """ The main function of Bucket sort
    """
    def __init__(self, data_list, length):
        self.data_list = data_list
        self.length = length

    def sort(self):
        bucket = []
        for i in xrange(length):
            node = Node()
            bucket.append(node)
        for data in self.data_list:
            node = Node()
            node.data = data
            number = int(floor(10*data))
            if bucket[number].next == None:
                bucket[number].next = node
            else:
                p = bucket[number]
                q = p.next
                while q != None and q.data < node.data:
                    p = p.next
                    q = q.next
                p.next = node
                node.next = q
        # Store all the sorted data in data_list
        data_list = []
        for i in xrange(length):
            p = bucket[i].next
            if p == None:
                continue
            else:
               while p != None:
                    data_list.append(p.data)
                    p = p.next
        print data_list

if __name__ == "__main__":
    data_list = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68, 0.19]
    length = 10
    bucket_sort = BucketSort(data_list, length)
    bucket_sort.sort()
