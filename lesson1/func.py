def get_summ(one, two, delimiter='&'):
    result = f"{str(one)}{delimiter}{str(two)}"
    return result.upper()


print(get_summ(1, 2, "/"))
print(get_summ("Learn", "python"))
