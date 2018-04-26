from textblob import TextBlob as tb
from textblob import Word
import numpy as np
import pandas as pd

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

with open('gg.txt') as f:
    text= f.read()
text= tb(text)
j= list()
for i in text.sentences:
    j.append(i)
"""text= tb(Last year saw machine learning continue to be at the forefront of technological innovation, with a number of eye-catching projects coming to fruition. Arguably the most well-publicized was Google DeepMind’s AlphaGo defeat of 9-dan professional Go star Lee Sedol in a five-game match, but the huge success of consumer products such as Amazon’s Alexa probably have more long-term ramifications for AI in everyday life. As Amazon chief Jeff Bezos told the Internet Association’s annual gala in Washington DC, ‘It is a renaissance, it is a golden age. We are now solving problems with machine learning and artificial intelligence that were in the realm of science fiction for the last several decades. And natural language understanding, machine vision problems, it really is an amazing renaissance’.

‘It will empower and improve every business, every government organization, every philanthropy,’ Bezos continued, ‘basically there’s no institution in the world that cannot be improved with machine learning’. And you would be hard pressed to find anyone who disagrees with him. In 2017, there is unlikely to be any let-up in the speed of innovation, as the biggest players in tech continue to invest heavily in the field. We’ve looked at some of the more interesting developments in the field.

We’ve had a look at some of the most exciting developments arising in machine learning this year, and also asked four machine learning experts from some of the world’s leading companies what was giving them cause for excitement in the field. As we saw in the recent WannaCry attacks, cybersecurity poses a clear and present danger to organizations in every industry and in truth, it is unlikely to be resolved anytime soon. Research by Accenture found that the average organization faces 106 targeted cyber-attacks per year, with one in three of those attacks resulting in a security breach. Towards the end of 2016, estimates put the number of new malware samples being generated in a single quarter at around 18 million - as many as 200,000 per day.

This threat is constantly mutating, as hackers adapt to cybersecurity measures and find new ways to infect systems. In order to deal with this, organizations must be extremely quick to adapt their security countermeasures, and machine learning techniques are the only technology currently available with this capability. Former Department of Defense Chief Information Officer, Terry Halvorsen, believes that ‘within the next 18-months, AI will become a key factor in helping human analysts make decisions about what to do’. This point of view is being reinforced by significant investment in the field by the world’s largest technology companies’. According to DFLabs’s May 2017 report ‘Next Generation Cybersecurity Analytics and Operations Survey,’ 93% of IT leaders are using or planning to use these types of solutions, 12% have deployed machine learning technologies designed for security analytics and operations automation and orchestration, 27% that they're doing so on a limited basis, and 22% said they're adding them. Just 6% said they're either not planning on or not interested in deploying these technologies.

MIT has been experimenting with it for some years, while IBM is training its AI-based Watson in security protocols and has now made it available to customers. Amazon also recently acquired AI-based cyber-security company Harvest.ai, which uses AI-based algorithms to identify the most important documents and intellectual property of a business before combining user behavior analytics with data loss prevention techniques.)
"""

dataset= pd.read_csv('ml_data_set.csv')
X= dataset.iloc[:,:].values
t= pd.DataFrame(X)
"""for x in f:
    for r in text.sentences:
        if x in r:
            print (r)
"""            
l= list()
copy= list()
ans= list()

for i in range(0,405):
    l.append(''.join(map(str,X[i])))

l= Remove(l)
for p in l:
    copy.append(p)

"""for r in l:
    for x in text.sentences:
        if r in x:
            ans.append(x)
"""
#y=['machine','IBM','classification','technology','specifications','Jeff','Bezos']
for x in text.sentences:
    for r in l:
        if r in x:
            ans.append(x)
            
listed= Remove(ans)
w= list()
for u in listed:
    w.append(''.join(map(str,u)))
lipo= list()
for i in w:
    t= tb(i)
    if(t.sentiment.subjectivity>0.1):
        lipo.append(''.join(map(str,t)))

for n in lipo:
    print(n)

            