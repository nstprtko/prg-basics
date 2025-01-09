class Statistiks:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def display_numbers(self):
        if self.numbers :
            return "Numbers:" + " ".join(map(str, self.numbers))
        else:
            return "No numbers added yet"
        
    def get_min(self):
        if self.numbers:
            return min(self.numbers)
        else:
            None

    def get_max(self):
        if self.numbers :
            return max(self.numbers)
        else:
            None

    def mean(self):
        return sum(self.numbers)/len(self.numbers) if self.numbers else None

    def median(self):
        if not self.numbers:
            return None

        sorted_numbers = sorted(self.numbers)
        n = len(sorted_numbers)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_numbers[mid - 1] + sorted_numbers[mid])/2
        else:
            return sorted_numbers[mid]
        
    def __str__(self):
        if not self.numbers:
            return "No numbers"
        
        stats =[ f"Minmum : {self.get_min()}",
                f"Maximum : {self.get_max()}",
                f"Mean : {self.mean():.2f}",
                f"Median : {self.median():.2f}"
                ]

        return "\n".join(stats)
    
def main():
    stats = Statistiks()
    numbers = [12, 37, 6, 9, 17]
    for num in numbers:
        stats.add_number(num)

    results = []
    results.append(stats.display_numbers())
    results.append(str(stats))

    return "\n".join(results)

if __name__ == "__main__":
    print(main())


                
