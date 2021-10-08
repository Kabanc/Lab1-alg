class Array:

    def __init__(self):
        self.capacity = 2
        self._array = [None] * self.capacity
        self.count = 0

    def __len__(self):
        i = 0
        for el in self._array:
            i += 1
        return i

    def __str__(self):
        output = ""
        for i in range(self.count):
            output += str(self._array[i]) + ","

        return output[:-1]

    def _increaseCapacity(self, newCapacity):
        if newCapacity < self.capacity:
            raise ValueError("Новый capacity не может быть ниже настоящего")

        newAr = [None] * newCapacity

        i = 0
        for el in self._array:
            newAr[i] = el
            i += 1

        self.capacity = newCapacity
        self._array = newAr

    def get(self, order):
        return self.get(order)

    def add(self, value):
        if self.count >= self.capacity:
            self._increaseCapacity(self.capacity * 2)

        self._array[self.count] = value
        self.count += 1

    def set(self, order, value):
        self._array[order] = value

    def orderOf(self, value):
        i = 0
        for el in self._array:
            if el == value:
                return i
            i += 1

        return -1

    def remove(self, value):
        order = self.orderOf(value)
        if order == -1:
            raise ValueError("Value not found")

        self.removeAt(order)

    def removeAt(self, order):
        if order < 0 or order >= self.count:
            raise IndexError("Некорректный номер элемента")

        self.count -= 1
        for i in range(order, self.count):
            self._array[i] = self._array[i+1]

        self._array[self.count] = None

    def isEmpty(self):
        return self.count == 0
