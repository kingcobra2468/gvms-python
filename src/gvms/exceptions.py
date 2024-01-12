class GVMSRequestException(IOError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return self.message
