def validate_expression(expression):
    valid_characters = '0123456789+-*/^xX()'
    last_character = ''
    expression = expression.replace(" ", "")
    expression = expression.replace("+-", "-")
    expression = expression.replace("--", "+")

    # Stack to keep track of opening parentheses
    stack = []

    for character in expression:
        if character not in valid_characters:
            return False, expression
        # Handle the case when "()" is missing multiplication
        if character == '(' and last_character in '0123456789xX':
            expression = expression.replace(last_character + '(', last_character + '*(')

        # Check for balanced parentheses
        if character == '(':
            stack.append(character)
        elif character == ')':
            if not stack:
                return False, expression
            stack.pop()

        if character in '+*/^' and last_character in '+-*/^(':
            return False, expression
        if character == 'x' and last_character in '0123456789x)' and last_character not in '':
            expression = expression.replace(last_character + 'x', last_character + '*x')
        last_character = character

    # Check if parentheses are balanced
    if stack:
        return False, expression

    if last_character in '+-*/^(':
        return False, expression

    expression = expression.replace("^", "**")

    return True, expression

def get_points(function, min , max):
    x_axis = []
    y_axis = []
    for i in range(100):
        x = min + (max - min) * i / 100
        x_axis.append(x)
        try:
            result = eval(function)
            if isinstance(result, (int, float)):
                y_axis.append(result)
            else:
                y_axis.append(float('nan'))
        except ZeroDivisionError:
            y_axis.append(float('inf'))
    return x_axis, y_axis

