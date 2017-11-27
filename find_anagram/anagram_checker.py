import sys


class AnagramCheck:
    def __init__(self):
        pass

    def is_anagram(self, a, b):
        # remove all non alphanum chars in string
        new_a = "".join([x for x in a.lower() if x.isalnum()])
        new_b = "".join([x for x in b.lower() if x.isalnum()])
        if len(new_a) != len(new_b):
            return False

        a_dict = {}
        b_dict = {}
        for char in new_a:
            a_dict[char] = a_dict.get(char, 0) + 1
        for char in new_b:
            b_dict[char] = b_dict.get(char, 0) + 1
        return b_dict == a_dict


class AnagramTester:
    def __init__(self):
        pass

    def test_is_anagram_with_file(self, filename):
        results = {}
        anagram_checker = AnagramCheck()
        with open(filename) as f:
            content = f.readlines()

        for line in content:
            line_list = line.strip().split('","')
            results[anagram_checker.is_anagram(line_list[0][1:], line_list[1][:-1])] = results.get(
                anagram_checker.is_anagram(line_list[0][1:], line_list[1][:-1]), 0) + 1

        return results

def main():
    if len(sys.argv) == 3:
        checker = AnagramCheck()
        print checker.is_anagram(sys.argv[1],sys.argv[2])

if __name__ == '__main__':
    main()