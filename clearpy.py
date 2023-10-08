def mystery_function(n):
    if n<4:
        return n
    return mystery_function(n-1)+mystery_function(n-2)
result=mystery_function(6)


#13