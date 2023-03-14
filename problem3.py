def push_letters(string):
    output = ''
    for i, char in enumerate(string):
        spaces = i
        if char != 'A':
            spaces += ord(char) - ord('A')
        output = output[:spaces] + char + output[spaces+1:]
    return output.rjust(len(string))

# Exemples d'utilisation
print(push_letters("AZ"))  # Attendu : "A                         Z"
print(push_letters("ABC"))  # Attendu : "A B C"
print(push_letters("ACE"))  # Attendu : "A  C  E"
print(push_letters("CBA"))  # Attendu : "  A"
print(push_letters("HELLOWORLD"))  # Attendu : "     E H    DLL   OLO   R  W"
