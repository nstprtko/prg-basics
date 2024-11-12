def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_in(n):
    return n/2.54

def feet_in_to_cm(f, i):
    in_to_cm = i*2.54
    fe_to_cm = f * 30.48
    return in_to_cm + fe_to_cm


if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')

