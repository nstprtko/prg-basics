class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority
        self.result = ''
    
    def generate_result(self):
        if self.age >= 18:
            upper_surname = self.surname.upper()
            first_letter = self.name[0].upper()
            seniority = str(self.seniority)
            sum = [upper_surname, first_letter, seniority]
            return "".join(sum)
        else:
            lower_surname = self.surname.lower()
            first_letter = self.name[0].lower()
            seniority = str(self.seniority)
            sum = [lower_surname, first_letter, seniority]
            return "".join(sum)
        
def main():
    obj = C("Anna","May",17,7)
    obj1=C("George","Brown",21,4)
    result = obj.generate_result()
    result1 = obj1.generate_result()
    print(result)
    print(result1)
    
if __name__=="__main__":
    main()
        