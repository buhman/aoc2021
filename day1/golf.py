def golf(text):
    nums = list(map(int, text.split("\n")))
    return sum(
        map(lambda ix: int(nums[ix - 1] < nums[ix]),
            range(1, len(nums)))
    )
