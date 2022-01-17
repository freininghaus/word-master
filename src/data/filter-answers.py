#!/usr/bin/env python3

import sys

union = set()
intersction = None


def is_good_word(word):
    return (len(word) == 5 and
            all(ord(c) >= ord('a') and ord(c) <= ord('z') for c in word) and
            word not in ('break', 'class', 'super'))


for path in sys.argv[1:]:
    with open(path) as f:
        new_words = set(word
                        for word in (line.strip().lower() for line in f)
                        if is_good_word(word))

        union |= new_words

        if intersction is None:
            intersction = new_words
        else:
            intersction &= new_words


blacklist = set(("siels",))
intersction -= blacklist


with open("answers.js", "w") as f:
    f.write("const answers = [\n")
    for word in sorted(intersction):
        f.write("  '{}',\n".format(word))

    f.write("]\n\nexport default answers")


with open("words.js", "w") as f:
    f.write("const words = {\n")
    for word in sorted(union):
        f.write("  {}: true,\n".format(word))

    f.write("}\n\nexport default words")
