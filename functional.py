def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

    # the data is immutable because there are no lists or dictionaries 

    # the function is pure because the output is exactly what it intends to be

    # it is not a higher order function because there is not function defined inside of the original function

    # no this works very well in python i think

    # to organize the data and take any number of inputs for variety and flexibility 