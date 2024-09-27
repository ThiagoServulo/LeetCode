def interpret(command):
    command = command.replace('(al)', 'al')
    command = command.replace('()', 'o')
    return command

print(interpret("G()()()()(al)"))