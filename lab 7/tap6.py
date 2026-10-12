def list_sum(values):
    total = 0
    for v in values:
        total += v
    return total

def list_average(values):
    if not values:
        return None
    return list_sum(values) / len(values)

def list_min_max(values):
    if not values:
        return None, None
    mini = max_val = values[0]
    for v in values[1:]:
        if v < mini:
            mini = v
        if v > max_val:
            max_val = v
    return mini, max_val

def count_by_sign(values):
    pos = neg = z = 0
    for v in values:
        if v > 0: pos += 1
        elif v < 0: neg += 1
        else: z += 1
    return pos, neg, z

def transform(values):
    return [v ** 2 for v in values]
