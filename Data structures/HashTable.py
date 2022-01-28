class Calendar(HashTable):
    def __init__(self, days):
        super().__init__(days)

    def __len__(self):
        return self.count

    def sum_temperature(self):
        result = 0
        for i in range(self.__len__()):
            if self.calendar[i] is not None:
                result += self.calendar[i].sum()
        return result


if __name__ == '__main__':
    import csv, array

    table = Calendar(13)
    file = open("../Help/data_structures/4_HashTable_2_Collisions/Solution/nyc_weather.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        if row[0] is not None:
            table[row[0]] = int(row[1])
    print(table.sum_temperature())
    from Linked_lists import LinkedList


    class HashTable(LinkedList):
        """
        A hash table is a data structure that calculates a specific value to a given key, and then inputs it in an
        array.
        On the basis of hash tables, python's dictionary was written.
        """
        def __init__(self, count):
            self.count = count
            self.calendar = [None for i in range(self.count)]

        def get_address(self, key):
            key = sum(ord(i) for i in key)
            return key % self.count

        def __setitem__(self, key, value):
            key = self.get_adress(key)
            if self.calendar[key] is None:
                self.calendar[key] = LinkedList()
                self.calendar[key].insert_at_beginning(value)
            else:
                self.calendar[key].insert_at_beginning(value)

        def __str__(self):
            result = ""
            for linkedlist in self.calendar:
                result += str(linkedlist) + "\n"
            return result

        def __delitem__(self, key):
            self.calendar[self.get_adress(key)] = None


