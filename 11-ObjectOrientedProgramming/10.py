class C:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def m(self, n):
        count = sum(1 for x, y in self.coordinates if x > 0 and y > 0)
        return count >= n
    
    def __str__(self):
        return f"Coordinates: {self.coordinates}, m(2): {self.m(2)}"

def main():
    obj = C([[2, 3], [1, 8], [-6, 4], [3, -7]])  
    result = obj.m(2)
    return result
if __name__=='__main__':
    results = main()
    print(results)
    