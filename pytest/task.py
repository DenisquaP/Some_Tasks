def solution(args):
    end_str = ''
    subsequence = [args[0]]  # if args[0] == args[1] + 1 else []
    for i in args[1:]:
        if i != subsequence[-1] + 1:
            if len(subsequence) > 2:
                end_str += '-'.join([str(subsequence[0]), str(subsequence[-1])])  # noqa 501
                end_str += ','
            else:
                end_str += ','.join(map(str, subsequence))
                end_str += ',' if end_str[-1] != ',' else ''
            subsequence = [i]
        else:
            subsequence += [i]
    if len(subsequence) > 2:
        end_str += '-'.join([str(subsequence[0]), str(subsequence[-1])])
        return end_str
    end_str += ','.join(map(str, subsequence))
    return end_str
