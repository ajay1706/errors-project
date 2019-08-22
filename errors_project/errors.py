class MyCustomError(TypeError):
    """"
    Exception is raised when a specific error code is needed

    """
    def __init__(self,message,code):
        super().__init__(f'Error code {code} : {message}')
        self.code = code
err = MyCustomError('An error occured',500)
print(err)


class UncountableError(ValueError):
    def __init__(self, wrong_value):
        super().__init__('Invalid value for n, {}. n must be greater than 0.'.format(wrong_value))


# do not change anything in the count_from_zero_to_n() function
# you may expect your UncountableError work in the following way
def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)
err1 = UncountableError(-10)
print(err1)