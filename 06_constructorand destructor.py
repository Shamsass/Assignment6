class Logger:
    def __init__(self):
         print("Object created")   #constructor 

    def __del__(self):
         print("Object destroyed")    #destructor

if __name__ == "__main__":
   log = Logger()
   del log
