from helpers import loadFile
input = loadFile(__file__)

def has_safe_changes(sorted_report, threshold):
    for it in range(len(sorted_report) - 1):
        if abs(sorted_report[it] - sorted_report[it + 1]) > threshold:
            return False
    return True

def is_safe_only_asc_or_desc(report):
    if len(set(report)) != len(report):
        return False

    asc = sorted(report)
    if report == asc:
        return has_safe_changes(asc, 3)

    desc = sorted(report,reverse=True)
    if report == desc:
        return has_safe_changes(desc, 3)

    return False

reports = [[int(v) for v in r.split()] for r in input]

result = len([safe for safe in [is_safe_only_asc_or_desc(r) for r in reports] if safe])
print(result)
