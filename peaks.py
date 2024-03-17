def solution(A):
    peaks = []
    #enumerate A to access its indexes and values. Loop through A checking if a given value is greater than the 2 around it.
    for index,value in enumerate(A):
        #if a value is greater than the value before and after it. It is a peak and we append it's index to peaks
        if(A[index-1] < value > A[index+1]):
            peaks.append(index)

    #start no. of flags at 1 if peaks is not empty
    # flags = len(peaks) or 0
    
    # if peaks[1] - peaks[0] >= flags+1:
    #     flags += 1
    # if peaks[1] - peaks[0] >= flags+1:
    #     flags += 1
    # else:
    #     if peaks[2] - peaks[0] >= flags+1:
    #         if peaks[3] - peaks[2] >= flags+1:
    #             flags += 1

    #let's loop through peaks accessing the values in each postition. This time using i to access the index.
    print(peaks)
    last_flag = peaks[len(peaks) - 1]

    initial_flags = peaks

    flags = len(peaks)

    j = 0
    i = 1
    while i < len(peaks) - 1:
        if peaks[i] == 0:
            i += 1
        if peaks[i] - peaks[j] < flags:
            flags -= 1
            peaks[i] = 0
            i = j + 1
        if peaks[i] - peaks[i-1] >= flags:
            j = i
            i += 1
        if peaks[len(peaks) - 1] == 0:
            peaks[j] = 0
            peaks[len(peaks) - 1] = last_flag
        if i == len(peaks) - 1:
            current_flags = peaks
        print(peaks)

    

    print(flags)
    return flags

#solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2])
solution([1, 4, 6, 7, 13, 16, 19])