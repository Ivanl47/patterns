class VariableConst:
    
    EMPTY_STRING_OPTION = ["", "None", "none", "N/A", "n/a", "null", "NULL", " ", None]
    EMPTY_FLOAT_OPTION = [-999.0, None]
    EMPTY_INT = None
    
    EXEPTIONS_TEXT = {
        'ID_NONE': "ID cannot be None",
        'ID_NEGATIVE': "ID must be a positive integer",
        'ID_NOT_FOUND': "ID not found",
        'NO_ONE_CAN_BE_NONE': "None value is not allowed",
        'ONE_CAN_BE_NOT_NONE': "At least one field must be not None",
        'NO_CHANGES': "No changes detected",
        'ALREADY_EXISTS': "Already exists",
    }
    
    

    
    