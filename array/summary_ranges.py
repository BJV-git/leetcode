def summaryRanges(nums):
    res = []
    result = []
    if nums:

        len_nums = len(nums)
        if len_nums == 1:
            result = result.append((str(nums[0])))
            print(result)
            return result
        else:
            distance = [(nums[i + 1] - nums[i]) for i in range(len_nums - 1)]
            print(distance)
            if not any(v != 1 for v in distance):
                result = str(nums[0]) + '->' + str(nums[len_nums-1])
                print(result)
                return result
            indexes = [i for i in range(len(distance)) if distance[i] != 1]
            res = []
            res.append([0, indexes[0]])
            ranges = [[indexes[i] + 1, indexes[i + 1]] for i in range(len(indexes) - 1)]
            res.extend(ranges)
            res.append([indexes[-1] + 1, len(nums) - 1])
            result = [str(nums[i]) + '->' + str(nums[j]) if i != j else str(nums[i]) for i, j in res]

    print(result)
    return result

summaryRanges([0,1,2])
