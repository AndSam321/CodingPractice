def change(st):
    result = ""
    new_string = st.lower() 
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter in new_string:
            result += "1"
        else:
            result += "0"
            
    return result