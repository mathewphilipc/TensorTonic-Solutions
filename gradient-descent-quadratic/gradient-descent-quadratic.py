def single_grad_step(a, b, x0, lr):
    """
    Perform a single gradient descent step for the function
    f(x) = ax^2 + bx + c, starting at x0, with step size lr.
    Note that f'(x) = 2ax + b.
    """
    fprime = 2*a*x0 + b
    return x0 - lr*fprime

def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    curr_x = x0
    for step in range(steps):
            curr_x = single_grad_step(a, b, curr_x, lr)
    return curr_x