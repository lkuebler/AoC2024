from utils import download_aoc_input_as_string

input_str = download_aoc_input_as_string(day=5)

input_str = "47|53\n97|13\n97|61\n97|47\n75|29\n61|13\n75|53\n29|13\n97|29\n53|29\n61|53\n97|53\n61|29\n47|13\n75|47\n97|75\n47|61\n75|61\n47|29\n75|13\n53|13\n\n75,47,61,53,29\n97,61,53,29,13\n75,29,13\n75,97,47,61,53\n61,13,29\n97,13,75,29,47"

# part 1
incorrect = []
rules = []
total_sum = 0
for line in input_str.splitlines():
    if "|" in line:
        before, after = list(map(int, line.split("|")))
        rules.append((before, after))
    elif "," in line:
        pages = list(map(int, line.split(",")))
        valid = True
        for idx, page in enumerate(pages):
            filtered = list(filter(lambda x: x[0] == page or x[1] == page, rules))
            for rule in filtered:
                before, after = rule
                if before in pages and after in pages:
                    before_idx = pages.index(before)
                    after_idx = pages.index(after)
                    if before_idx > after_idx:
                        valid = False
                        break
            if not valid:
                break
        if valid:
            mid = pages[int((len(pages)-1)/2)]
            total_sum += mid
        else:
            incorrect.append(pages)

print(f"part 1: {total_sum}")