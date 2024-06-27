calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    counter = 0
    for i in string:
        counter += 1
    return counter, string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.lower() in i.lower() or i.lower() in string.lower():
            return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
