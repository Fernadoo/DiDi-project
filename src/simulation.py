import random
import time
class Car:
    def __init__(self, available, now_region, preferred_region, name):
        self.available = available
        self.now_region = now_region
        self.preferred_region = preferred_region
        self.name = name
        self.to_go = -1

    def whether_can_go(self,wanted_region):
        if (self.available):
            if (abs(self.now_region-wanted_region)+abs(self.now_region-wanted_region))<=4:
                if (wanted_region in self.preferred_region):
                    if (self.to_go==-1):
                        return True
        return False


class Region:
    def __init__(self, predicted_car, region1, now_car=[]):
        self.predicted_car = predicted_car
        self.now_car = now_car
        self.need_car = abs(predicted_car-len(now_car))
        self.region = region1

    def lack_or_more(self):
        if (self.predicted_car<self.now_car):
            return False,len(self.now_car)-self.predicted_car
        else:
            return True, self.predicted_car-len(self.now_car)

    def add_car(self,car):
        self.now_car.append(car)
        self.need_car -= 1



class ZHeap:
    def __init__(self, item=[]):
        self.items = item
        self.heapsize = len(self.items)

    def LEFT(self, i):
        return 2 * i + 1

    def RIGHT(self, i):
        return 2 * i + 2

    def PARENT(self, i):
        return (i - 1) // 2

    def MIN_HEAPIFY(self, i):
        l = self.LEFT(i)
        r = self.RIGHT(i)
        if l < self.heapsize and self.items[l].need_car > self.items[i].need_car:
            largest = l
        else:
            largest = i

        if r < self.heapsize and self.items[r].need_car > self.items[largest].need_car:
            largest = r

        if largest != i:
            self.items[i], self.items[largest] = self.items[largest], self.items[i]
            self.MIN_HEAPIFY(largest)

    def INSERT(self, val):
        self.items.append(val)
        idx = len(self.items) - 1
        parIdx = self.PARENT(idx)
        while parIdx >= 0:
            if self.items[parIdx].need_car < self.items[idx].need_car:
                self.items[parIdx], self.items[idx] = self.items[idx], self.items[parIdx]
                idx = parIdx
                parIdx = self.PARENT(parIdx)
            else:
                break
        self.heapsize += 1

    def DELETE(self):
        last = len(self.items) - 1
        if last < 0:
            return None
        self.items[0], self.items[last] = self.items[last], self.items[0]
        val = self.items.pop()
        self.heapsize -= 1
        self.MIN_HEAPIFY(0)
        return val

    def BUILD_MIN_HEAP(self):
        i = self.PARENT(len(self.items) - 1)
        while i >= 0:
            self.MIN_HEAPIFY(i)
            i -= 1

    def SHOW(self):
        print(self.items)


class ZPriorityQ(ZHeap):
    def __init__(self, item=[]):
        ZHeap.__init__(self, item)

    def insert(self, val):
        ZHeap.INSERT(self, val)

    def pop(self):
        val = ZHeap.DELETE(self)
        return val


region = []
predited_number = []
car_array = []
width = 4
height = 5
total = width*height
for i in range(total):
    region_ = Region(predited_number[i], (i % width, i//width))
    region.append(region_)

for i in range(len(car_array)):
    car_ = Car(random.randint(0,1),(car_array[i][1] % width, car_array[i][1]//width),car_array[i][2],car_array[i][0])
    region[car_array[i][1]].add_car(car_)

need_car = ZPriorityQ()
more_car = ZPriorityQ()
for i in range(total):
    a,b = region[i].lack_or_more()
    if (a):
        need_car.insert(region[i])
    else:
        more_car.insert(region[i])

while (1):
    a = need_car.pop()
    b = more_car.pop()
    if (abs(a.region[0]-b.region[0])+abs(a.region[1]-b.region[1]))>=4:
        c = b
        b = more_car.pop()
        more_car.insert(c)
    for i in range(len(b.now_car)):
        if (b.now_car[i].whether_can_go(a.region)):
            input1 = input("Whether you want to go to Region (%d,%d)"%(a.region[0],a.region[1]))
            a.add_car(b.now_car[i])
            b.now_car.remove(i)
            b.need_car += 1
    time.sleep(10)



















