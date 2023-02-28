def starcase(number):
    result = ""
    for i in range(1, number+1):
        result += f'{"#"*i:>{number}}\n'

    return result.rstrip()