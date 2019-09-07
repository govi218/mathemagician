def get_polynomial_value_for_x(coeffs,x=0):
    degree = len(coeffs) - 1
    val = 0
    for i in range(len(coeffs) - 1):
        curr_degree = degree
        val = val + x**curr_degree * coeffs[i]
        degree = degree - 1
    return val + coeffs[len(coeffs) - 1]
    
def mathemagician(coeffs):
    one_val = get_polynomial_value_for_x(coeffs,1)
    higher = get_polynomial_value_for_x(coeffs,one_val + 1)
    poly_coeffs = ''
    i = 0
    while(higher > 0):
        poly_coeffs += '+' + str(higher % (one_val+1)) + 'x^' + str(i)
        higher  = higher // (one_val+1)
        i = i+1
    return(poly_coeffs[1:])
