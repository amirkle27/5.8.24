def str_opr (word: str = "", operation: str = "") -> str:
    """Gets a string and an operation from the user and returns string after operation"""
    word: str= str(input("Please enter a word"))
    operation: str = str (input("Please enter the needed operation: (lower, upper, len, reverse)"))
    oper_dict: dict = {"lower": word.lower(), "upper": word.upper(), "len": len(word), "reverse": word [::-1]}
    oper = oper_dict.get(operation)
    return print(oper)


str_opr("go")
