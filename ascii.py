def decrypt(message : [int]) -> str:
    """
    Decrypt a message from a list of integers to ascii characters
    :param message:
    :return:
    """
    return "".join([chr(i) for i in message])