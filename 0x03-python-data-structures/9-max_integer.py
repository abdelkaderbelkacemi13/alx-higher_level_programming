#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) != 0:
        m_int = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > m_int:
                m_int = my_list[i]
    else:
        return (None)
    return (m_int)
