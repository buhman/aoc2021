def iterative(text):
    numbers = text.split("\n")
    last = None
    count = 0
    for number in numbers:
        this = int(number)
        if not last:
            last = this
            continue
        count += int(last < this)
        last = this
    return count
