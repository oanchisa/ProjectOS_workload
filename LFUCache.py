import collections

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # เก็บข้อมูลในแคช
        self.frequency = {}  # เก็บความถี่การใช้งานของข้อมูล
        self.min_frequency = 0  # เก็บความถี่ที่น้อยที่สุดในแคช

    def get(self, key):
        if key in self.cache:
            # ถ้า key อยู่ในแคช
            # อัพเดทความถี่การใช้งานของ key
            self.frequency[key] += 1
            # อัพเดทความถี่ที่น้อยที่สุด
            self.min_frequency = min(self.min_frequency, self.frequency[key])
            return self.cache[key]
        else:
            return -1  # หากไม่พบ key ในแคช

    def put(self, key, value):
        if self.capacity > 0:
            if key in self.cache:
                # ถ้า key อยู่ในแคช
                # อัพเดทความถี่การใช้งานของ key
                self.frequency[key] += 1
                # อัพเดทความถี่ที่น้อยที่สุด
                self.min_frequency = min(self.min_frequency, self.frequency[key])
                self.cache[key] = value
            else:
                if len(self.cache) >= self.capacity:
                    # ถ้าแคชเต็ม
                    # ลบข้อมูลที่ความถี่การใช้งานน้อยที่สุด
                    while self.min_frequency not in self.frequency:
                        self.min_frequency += 1
                    key_to_remove = None
                    for k, v in self.cache.items():
                        if self.frequency[k] == self.min_frequency:
                            key_to_remove = k
                            break
                    if key_to_remove is not None:
                        del self.cache[key_to_remove]
                        del self.frequency[key_to_remove]

                # เพิ่มข้อมูลใหม่ลงในแคช
                self.cache[key] = value
                self.frequency[key] = 1
                self.min_frequency = 1

# ตัวอย่างการใช้งาน
cache = LFUCache(2)  # สร้างแคชขนาด 2

cache.put(1, 'A')
cache.put(2, 'B')

print(cache.get(1))  # ผลลัพธ์: 'A' (เพราะ '1' ถูกใช้งานครั้งเดียว)
print(cache.get(2))  # ผลลัพธ์: 'B' (เพราะ '2' ถูกใช้งานครั้งเดียว)
print(cache.get(3))  # ผลลัพธ์: -1 (ไม่พบข้อมูล '3' ในแคช)
