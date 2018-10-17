# -*- coding: utf-8 -*-

import json
import itchat


itchat.login()

friends = itchat.get_friends(update=True)[0:]

total = len(friends[1:])

print(total)

# fileObject = open('ex99List.txt', 'w')

# for friend_info in friends[1:]:
#     fileObject.write(friends[1:])
#     fileObject.write('\n')
# fileObject.close()


with open('ex98.json', 'w') as f:
        f.write(json.dumps(friends[1:]))
        f.close()
