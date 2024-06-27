#Build an Arithmetic Formatter Project
#Students in primary school often arrange arithmetic problems vertically to
#make them easier to solve. For example, "235 + 52" becomes:
#
#  235
#+  52
#-----
#Finish the arithmetic_arranger function that receives a list of strings which
#are arithmetic problems, and returns the problems arranged vertically and
#side-by-side. The function should optionally take a second argument. When the
#second argument is set to True, the answers should be displayed.
#
#Examples:
#Function Call:
#
#arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
#Output:
#
#   32      3801      45      123
#+ 698    -    2    + 43    +  49
#-----    ------    ----    -----
#Function Call:
#
#arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
#Output:
#
#  32         1      9999      523
#+  8    - 3801    + 9999    -  49
#----    ------    ------    -----
#  40     -3800     19998      474
#
#Rules
#The function will return the correct conversion if the supplied problems are
#properly formatted, otherwise, it will return a string that describes an error
#that is meaningful to the user.

#Situations that will return an error:
#-If there are too many problems supplied to the function. The limit is five,
#anything more will return: 'Error: Too many problems.'
#-The appropriate operators the function will accept are addition and
#subtraction. Multiplication and division will return an error. Other operators
#not mentioned in this bullet point will not need to be tested. The error returned will be: "Error: Operator must be '+' or '-'."
#-Each number (operand) should only contain digits. Otherwise, the function will
#return: 'Error: Numbers must only contain digits.'
#-Each operand (aka number on each side of the operator) has a max of four
#digits in width. Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'
#If the user supplied the correct format of problems, the conversion you return
#will follow these rules:
# -There should be a single space between the operator and the longest of the
#two operands, the operator will be on the same line as the second operand,
# both operands will be in the same order as provided (the first will be the
# top one and the second will be the bottom).
# -Numbers should be right-aligned.
# -There should be four spaces between each problem.
# -There should be dashes at the bottom of each problem. The dashes should run
# along the entire length of each problem individually. (The example above
# shows what this should look like.)





def arithmetic_arranger(problems, show_answers=False):
    output_line_1 = ''
    output_line_2 = ''
    output_line_3 = ''
    output_line_4 = ''
    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        line = '1'
        first = ''
        second = ''
        symbol = ''
        for char in problem:
            if char == '*' or char == '/':
                return "Error: Operator must be '+' or '-'."
            elif char.isalpha():
                return 'Error: Numbers must only contain digits.'
            elif char != '+' and char != '-' and char != ' ' and line == '1':
                first += char
            elif char != '+' and char != '-' and char != ' ' and line == '2':
                second += char
            elif char == '+' or char == '-':
                line = '2'
                symbol = char
        if len(first) > 4 or len(second) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if len(first) > len(second):
            length = len(first)
            white_space = len(first) - len(second)
            output_line_1 += '  ' + first + '    '
            output_line_2 += symbol + ' ' + ' ' * white_space + second + '    '
            output_line_3 += '-' * (len(first) + 2) + '    '
        elif len(first) < len(second):
            length = len(second)
            white_space = len(second) - len(first)
            output_line_1 += '  ' + ' ' * white_space + first + '    '
            output_line_2 += symbol + ' ' + second + '    '
            output_line_3 += '-' * (len(second) + 2) + '    '
        elif len(first) == len(second):
            length = len(second)
            output_line_1 += '  ' + first + '    '
            output_line_2 += symbol + ' ' + second + '    '
            output_line_3 += '-' * (len(first) + 2) + '    '
        
        if show_answers and symbol == '+':

            if len(str(int(first) + int(second))) == length:
                output_line_4 += '  ' + str(int(first) + int(second)) + '    '
                
            elif len(str(int(first) + int(second))) > length:
                space = len(str(int(first) + int(second))) - length
                output_line_4 += (' ' * space + str(int(first) + int(second))
                                  + '    ')

            elif len(str(int(first) + int(second))) < length:
                space = len(str(int(first) + int(second))) - length
                output_line_4 += ('  ' + ' ' * space
                                  + str(int(first) + int(second)) + '    ')
            
        elif show_answers and symbol == '-':
            if len(str(int(first) - int(second))) == length:
                output_line_4 += ' ' + str(int(first) - int(second)) + '    '

            elif len(str(int(first) - int(second))) > len(second):
                space = len(str(int(first) - int(second))) - length
                output_line_4 += (' ' * space + str(int(first) - int(second))
                                  + '    ')

            elif len(str(int(first) - int(second))) < length:
                space = len(str(int(first) - int(second))) - length
                output_line_4 += ('  ' + ' ' * space
                                  + str(int(first) - int(second)) + '    ')

    if show_answers:
        return (output_line_1.rstrip(' ') + '\n' + output_line_2.rstrip(' ')
                + '\n' + output_line_3.rstrip(' ')
                + '\n' + output_line_4.rstrip(' '))
    else:
        return (output_line_1.rstrip(' ') + '\n' + output_line_2.rstrip(' ')
                + '\n' + output_line_3.rstrip(' '))



         

print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
print('   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028')
