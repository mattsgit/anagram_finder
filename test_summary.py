from find_anagram import anagram_checker
import generate_anagrams

import os
import time


def main():
    counts = ['100', '1000', '10000', '100000']
    print 'Generating random anagram files. Each row has 2 strings of length 32-64 randomly sorted. ' \
          '"not" files have different character appended to each anagram to force false.'
    generate_starts = time.time()
    generate_anagrams.create_anagram_files(counts)
    print 'File generation took: %s seconds\n' % (time.time() - generate_starts)
    print 'Testing random files. Expect all True or False output for generated files and linear time and space complexity\n'

    anagram_tester = anagram_checker.AnagramTester()
    for file in os.listdir("anagram_files"):
        if file.endswith(".txt"):
            filename = 'anagram_files/%s' % file
            if os.name == 'nt':
                filename = 'anagram_files\%s' % file
            tester_starts = time.time()
            results = anagram_tester.test_is_anagram_with_file(filename)
            print 'Results are: %s. Took total of %s seconds to load and process file %s' % (
                results, time.time() - tester_starts, filename)


if __name__ == '__main__':
    main()
