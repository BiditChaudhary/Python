class employee:
    def __init__(self):
        print("An employee has been created.")
    
    def __del__(self):
        print("The employee has been deleted.")

emp1 = employee()
del emp1