vers = "We have seen thee, queen of cheese,\
Lying quietly at your ease,\
Gently fanned by evening breeze,\
Thy fair form no flies dare seize.\
All gaily dressed soon you'll go\
To the great Provincial show,\
To be admired by many a beau\
In the city of Toronto.\
Cows numerous as a swarm of bees,\
Or as the leaves upon the trees,\
It did require to make thee please,\
And stand unrivalled, queen of cheese.\
May you not receive a scar as\
We have heard that Mr. Harris\
Intends to send you off as far as\
The great world's show at Paris.\
Of the youth beware of these,\
For some of them might rudely squeeze \
And bite your cheek, then songs or glees \
We could not sing, oh! queen of cheese.\
We'rt thou suspended from balloon,\
You'd cast a shade even at noon,\
Folks would think it was the moon\
About to fall and crush them soon."

import re
# all words, which beginning of letter 'c'
print re.findall(r'\bc[a-z]*', vers, re.IGNORECASE)
# the same
print re.findall(r'\bc\w*', vers, re.I)
# all words, which beginning of letter 'c' and have four letters
print re.findall(r'\bc[a-z]{3}\b', vers, re.IGNORECASE)
# the same
print re.findall(r'\bc\w{3}\b', vers, re.I)
# all words, which ending of letter 'r'
print re.findall(r'\w+r\b', vers, re.IGNORECASE)
# all words, which ending of letter 'l'
print re.findall(r'[\'\w]+l\b', vers, re.IGNORECASE)
# the same
print re.findall(r"['\w]+l\b", vers, re.IGNORECASE)
# the words which have three consonant letters successively
print re.findall('\w*[aeiou]{3}\w*', vers, re.IGNORECASE)