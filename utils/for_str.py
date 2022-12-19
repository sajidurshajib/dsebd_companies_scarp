def string_handle(s):
    """ 
    this function handle empty value from a string.
    parameter s take string and for empty value set N/A 
    and strip the string 
    """

    if len(s) == 0:
        return 'N/A'
    elif s == '-':
        return 'N/A'
    else:
        return s.strip()
