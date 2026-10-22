# Daily Data Helper
 
# PART 1: Create a class with methods
class DailyMessage:
 
    # Constructor to set a default value
    def __init__(self):
        self.message = ""
 
    # Method to get input from the user
    def get_message(self):
        self.message = input("Enter today's message: ")
 
    # Method to print the message in uppercase
    def print_message(self):
        print("Message in uppercase:", self.message.upper())
 
 
# PART 2: Create an object and call methods
daily_text = DailyMessage()
daily_text.get_message()
daily_text.print_message()
 
 

class HelperSession:
 
   
    def __init__(self):
        print("Daily Data Helper session created")
 
    
    def __del__(self):
        print("Daily Data Helper session ended")
 
 
def create_session():
    print("Making helper session...")
    session = HelperSession()
    print("Session is ready...")
    return session
 
 
print("")
print("Calling create_session() function...")
session_obj = create_session()
print("Program is still running...")
 
 

 
def find_pair(self, numbers, target):
        lookup = {}
 
        for index, number in enumerate(numbers):
            needed_number = target - number
 
            if needed_number in lookup:
                return (lookup[needed_number], index)
 
            lookup[number] = index
 
        return None
 
 

numbers = (10, 20, 30, 40, 50, 60, 70)
 
target_value = int(input("Enter target sum to search: "))
 
result = PairFinder().find_pair(numbers, target_value)
 
if result is not None:
    print("index1=%d, index2=%d" % result)
else:
    print("No matching pair found.")
 

del session_obj
print("Program End")
