from collections import defaultdict


def create_graphs(synonyms):
    graphs = []
    for name, synonym in synonyms.items():
        inserted = False
        for graph in graphs:
            if name in graph:
                graph.add(synonym)
                inserted = True
            elif synonym in graph:
                graph.add(name)
                inserted = True
        if not inserted:
            new_set = set()
            new_set.add(name)
            new_set.add(synonym)
            graphs.append(new_set)
    return graphs


def babyNames(frequencies, synonyms):
    graphs = create_graphs(synonyms)
    result = defaultdict(int)

    visited = set()
    for name, f in frequencies.items():
        if name in visited:
            continue
        for g in graphs:
            if name in g:
                visited.add(name)
                for syn in g:
                    result[name] += frequencies[syn]
                    visited.add(syn)
                    # del frequencies[syn]
    for name, f in frequencies.items():
        if name not in visited:
            result[name] = f

    return result


test_case_number = 1


def printString(string):
    print('[\"', string, '\"]', sep='', end='')


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    frequencies = dict(
        John=10,
        Jon=10,
        Johnny=10,
        Carlton=5,
        Carleton=5,
        Kari=20,
        Cari=20,
        Davis=1
    )
    synonyms = dict(
        John='Jon',
        Jon='Johnny',
        Carlton='Carleton',
        Cari='Kari',
    )
    print(babyNames(frequencies, synonyms))
