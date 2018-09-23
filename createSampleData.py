import random
keys = ['parent_id', 'created_utc', 'score', 'body', 'name', 'subreddit']
randoms = ['adfa','ghr','bsdthrt','etb','beb','bebae','wref','erfge','rgjuj']
with open('Data','a',encoding='utf8', errors= 'ignore')as f:
    for i in range(1, 2000):
        line = """ "{0}":"{1}", "{2}":"{3}", "{4}":{5}, "{6}":"{7}", "{8}":"{9}", "{10}":"{11}" """.format(keys[0], random.choice(randoms),
                                                                                                           keys[1], i,
                                                                                                           keys[2], i,
                                                                                                           keys[3], random.choice(randoms),
                                                                                                           keys[4], random.choice(randoms),
                                                                                                           keys[5], random.choice(randoms))
        f.write("{"+line+"}")
        f.write("\n")
