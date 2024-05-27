def solution(A1, A2):
    if len(A1) < len(A2):
        return False
    elif A1[-len(A2):] == A2:
        return True
    else:
        return False
    
def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif a + b <= c or a + c <= b or b + c <= a:
        return False
    
    return True

def solution(text, ending):
    return text.endswith(ending)

def number(bus_stops):
    num_on_bus = 0

    
    for on, off in bus_stops:      
        num_on_bus += on
        num_on_bus -= off
        
    return num_on_bus