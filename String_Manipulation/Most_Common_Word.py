from typing import Counter
import re
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

word_cnt = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]
print(Counter(word_cnt).most_common(1)[0][0])