"""
import random

#yes = ['As I see it, yes.', 'It is certain.', 'It is decidedly so.', 'Most likely.', 'Outlook good.', 'Signs point to yes.', 'Without a doubt.', 'Yes.', 'Yes - definitely.', 'You may rely on it.']
#no  = ["Don't count on it.", 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
#maybe = ['Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Reply hazy, try again.']

ans = ['As I see it, yes., Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', "Don't count on it.", 'It is certain.', 'It is decidedly so.', 'Most likely.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Outlook good.', 'Reply hazy, try again.', 'Signs point to yes.', 'Very doubtful.', 'Without a doubt.', 'Yes.', 'Yes - definitely.', 'You may rely on it.']
i = 1

while i < 6:
    rng = random.randint(0,19)
    q = input("What's on your mind?\t")
    print(ans[rng])
"""
import random

lines = 4

while lines > 4:
    print(random.randint(1,40))