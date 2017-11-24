import string
import random

OTHER = '!@#      $%^&*()_          +=-[]{}     \|?>/.,<     `~'
COUNTS = ['100', '1000', '10000', '100000']


def id_generator(size, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + OTHER):
    return ''.join(random.choice(chars) for _ in range(size))


def create_anagram_files():
    for count in COUNTS:
        with open(r'anagram_files\%s_anagrams.txt' % count, 'w') as the_file:
            for i in xrange(1, int(count) + 1):
                size = (random.randint(32, 64))
                anagram = id_generator(size)
                the_file.write(
                    '"%s","%s"\n' % (''.join(random.sample(anagram, size)), ''.join(random.sample(anagram, size))))

        with open(r'anagram_files\%s_not_anagrams.txt' % count, 'w') as the_file:
            for i in xrange(1, int(count) + 1):
                size = (random.randint(32, 64))
                anagram = id_generator(size)
                the_file.write('"%s","%s"\n' % (''.join(random.sample(anagram[:1] + 'Z' + anagram[2:], size)),
                                                ''.join(random.sample(anagram[:1] + 'Y' + anagram[2:], size))))
