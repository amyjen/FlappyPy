def spam(times):
    return 'spam '*times
def multi_print(statement,times):
    for time in range(times):
        print(statement)
print(spam(10))
multi_print(spam(10),10)
