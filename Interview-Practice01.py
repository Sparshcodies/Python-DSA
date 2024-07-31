class Numbers():
    def findPrime(self):
        for i in range(10,15):
            isPrime = True
            for j in range(2,i//2):
                if i % j == 0:
                    isPrime = False
                    break
            if isPrime:
                print(i)
                
    def palindrome(self):
        str = input("Enter a number: ")
        if str == str[::-1]:
            print("Palindrome")
        else:
            print("Not Palindrome")
            
    def is_keyword(self):
        kw_list = ["break","case","continue","default","defer","for","else","elif","func","goto","if","map","range","return","struct","type","var"]
        str = "if"  # Replace input("Enter a keyword: ") with a hard-coded value for testing
        for word in str:
            if word in kw_list:
                print("Keyword")
                break
        else:
            print("Not Keyword")
            
def main():
    num = Numbers()
    # num.
    # num.palindrome()
    num.is_keyword()
    

if __name__ == "__main__":
    main()
