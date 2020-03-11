# coding: utf-8

import matplotlib.pyplot as plt
from matplotlib import font_manager as fm


# font
proptease = fm.FontProperties()
proptease.set_size('small')

labels = ['OS','exe','cache','container','data','log','free']
explode = (0,0,0,0,0,0,0.1)
values1 = [ 3,2,1,4,25,5,15]
values2 = [19,23,4,6,3,5,10]
values3 = [3,5,3,3,5,6,7]

#color
colors = ['#EB422C','#ED5D3B','#EF7F4D','#F29F61','#EEBC73','#DED685','#CBE897']

#main_pic
plt.figure(figsize=(5, 20))
plt.suptitle('disk space usage',fontsize=16)

#pic1
fig1 = plt.subplot(4,1,1)

plt.title('prod-1 ')
patches, texts, autotexts = plt.pie(values1, explode=explode, labels=labels, autopct='%1.0f%%',
        shadow=False, startangle=90,colors=colors)
plt.axis('equal')

plt.setp(autotexts, fontproperties=proptease)
plt.setp(texts, fontproperties=proptease)

#pic2
fig2 = plt.subplot(4,1,2)
plt.title('prod-2 ')
patches2, texts2, autotexts2 = plt.pie(values2, explode=explode, labels=labels, autopct='%1.0f%%',
        shadow=False, startangle=90,colors=colors)
plt.axis('equal')

plt.setp(autotexts2, fontproperties=proptease)
plt.setp(texts2, fontproperties=proptease)

#pic3
fig3 = plt.subplot(4,1,3)
plt.title('prod-3 ')
patches3, texts3, autotexts3 = plt.pie(values3, explode=explode, labels=labels, autopct='%1.0f%%',
        shadow=False, startangle=90,colors=colors)
plt.axis('equal')

plt.setp(autotexts3, fontproperties=proptease)
plt.setp(texts3, fontproperties=proptease)

#show

plt.savefig('./Demo_project.png')
plt.show()
