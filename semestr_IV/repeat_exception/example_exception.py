#raise
#try except else finally 
# __init__, __str__

class InputPositivException(Exception):
    """
    Клас винятку для функції введення з клавіатури додатніх чисел
    """
    def __init__(self,message, error_code,input_data, convert_data=None) ->None:
        """Конструктор
        :param message: повідомленн, яке виводиться при виникненні винятку

        """
        super().__init__(message)
        self.message=message
        self.error_code=error_code
        self.input_data=input_data
        self.convert_data=convert_data

    def __str__(self) -> str:
        return f"{self.message} error code {self.error_code}"


def input_positiv_number(*args):
    s=input(*args)    
    # if  type(s)!='int':
    #     raise InputPositivException("Це не ціле число",111,s)
    # elif type(s)=='int' and int(s)<0:
    #     raise InputPositivException("Це відємне число",222,s,int(s))
    # i=int(s)
    try:
        i=int(s)
    except ValueError:
        raise InputPositivException("Це не ціле число",111,s,None)
    if i<0:
        raise InputPositivException("Це відємне число",222,s,i)
    
    return i 


# Implementations
while True:
    try:
        data=input_positiv_number("Enter int number (exit => finish)")
        print(data)
    except InputPositivException as ex:
        if ex.error_code==111 and ex.input_data=="exit":
            break
        print(ex)
