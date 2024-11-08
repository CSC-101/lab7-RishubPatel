from typing import Optional

def str_to_float(string: str) -> Optional[float]: #Converts a given string to a float if possible; else returns None
    try:
        return float(string)
    except ValueError:
        return None
    except:
        return None