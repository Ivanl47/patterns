import functools

class LogerHelper:
    STATUS_DEBUG = True
    DEBUG_LEVEL = 3
    
    @staticmethod
    def log_to_file(text: str, debug_level: int) -> None:
        if debug_level <= LogerHelper.DEBUG_LEVEL and LogerHelper.STATUS_DEBUG:
            with open('log.txt', 'a', encoding='utf-8') as f:
                f.write(f"Log_file: {text}\n")
            
    
    @staticmethod
    def log_to_console(text: str, debug_level: int) -> None:
        if debug_level <= LogerHelper.DEBUG_LEVEL and LogerHelper.STATUS_DEBUG:
            print(f"Log_console: {text}")


def log_def(obj_name=""):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            obj_name_fmt = (" " + obj_name + " -> ") if obj_name else ""
            LogerHelper.log_to_file(f"Function called:{obj_name_fmt}func({func.__name__})", 1)
            return func(*args, **kwargs)
        return wrapper
    return decorator

