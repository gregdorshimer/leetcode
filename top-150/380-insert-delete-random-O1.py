import random

class RandomizedSet(object):

    def __init__(self):
        self.my_dict = dict()
        self.my_list = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.my_dict:
            return False
        else:
            self.my_dict[val] = len(self.my_list)
            self.my_list.append(val)
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.my_dict:
            index = self.my_dict.pop(val)
            if index < len(self.my_list) - 1:
                self.my_list[index] = self.my_list[-1]
                self.my_dict[self.my_list[index]] = index
            self.my_list.pop()
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        return self.my_list[random.randrange(len(self.my_list))]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()