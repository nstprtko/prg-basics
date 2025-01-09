class C:
    def __init__(self, sectors):
        self.sectors = sectors

    def m1(self, s, n):
        self.sectors[s] = n

    def m2(self, s):
        total_fans = sum(self.sectors.get(sector, 0) for sector in s)
        return total_fans
    

if __name__ == "__main__":
    stadium = C({"A": 120, "D": 150, "G": 90, "K": 110})
    
    # Update sector G to have 130 fans
    stadium.m1("G", 130)
    
    # Get the sum of fans in sectors G and D
    result1 = stadium.m2("GD")  # Should return 280
    print(result1)  # Output: 280
    
    # Get the sum of fans in sectors K, E, and J
    result2 = stadium.m2("KEJ")  # Should return 110 (K has 110, E and J are not in the dictionary)
    print(result2)  # Output: 110   
        