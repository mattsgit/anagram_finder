import os
import random
import string

OTHER = '!@#      $%^&*()_          +=-[]{}     \|?>/.,<     `~'


def id_generator(size, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + OTHER):
    return ''.join(random.choice(chars) for _ in range(size))


def create_anagram_files(counts):
    file_prefix = r'anagram_files/'
    if os.name == 'nt':
        file_prefix = r'anagram_files\\'
    for count in counts:
        with open(r'%s%s_anagrams.txt' % (file_prefix, count), 'w') as the_file:
            for i in xrange(1, int(count) + 1):
                size = (random.randint(32, 64))
                anagram = id_generator(size)
                the_file.write(
                    '"%s","%s"\n' % (''.join(random.sample(anagram, size)), ''.join(random.sample(anagram, size))))

        with open(r'%s%s_not_anagrams.txt' % (file_prefix, count), 'w') as the_file:
            for i in xrange(1, int(count) + 1):
                size = (random.randint(32, 64))
                anagram = id_generator(size)
                the_file.write('"%s","%s"\n' % (''.join(random.sample(anagram[:1] + 'Z' + anagram[2:], size)),
                                                ''.join(random.sample(anagram[:1] + 'Y' + anagram[2:], size))))
