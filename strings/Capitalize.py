def capitalize(string):
    s  = string
    for x in s.split():
        s = s.replace(x, x.capitalize())
    return (s)

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
