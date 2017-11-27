import os
import random
import string

# Symbols plus a large amount of spaces
OTHER = '!@#      $%^&*()_          +=-[]{}     \|?>/.,<     `~'

# generate random string of passed in size with all alphanumeric plus symbols and spaces from OTHER
def id_generator(size, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + OTHER):
    return ''.join(random.choice(chars) for _ in range(size))


# input is list of counts you want in each file
def create_anagram_files(counts):
    file_prefix = r'anagram_files/'
    # default linux, change to windows if needed
    if os.name == 'nt':
        file_prefix = r'anagram_files\\'
    for count in counts:
        with open(r'%s%s_anagrams.txt' % (file_prefix, count), 'w') as the_file:
            for i in xrange(1, int(count) + 1):
                size = (random.randint(32, 64))
                anagram = id_generator(size)
                # randomize the generated strings
                the_file.write(
                    '"%s","%s"\n' % (''.join(random.sample(anagram, size)), ''.join(random.sample(anagram, size))))

        with open(r'%s%s_not_anagrams.txt' % (file_prefix, count), 'w') as the_file:
            for i in xrange(1, int(count) + 1):
                size = (random.randint(32, 64))
                anagram = id_generator(size)
                # Force diff char into each string to make them not anagrams
                the_file.write('"%s","%s"\n' % (''.join(random.sample(anagram[:1] + 'Z' + anagram[2:], size)),
                                                ''.join(random.sample(anagram[:1] + 'Y' + anagram[2:], size))))
