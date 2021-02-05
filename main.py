from facebook_scraper import get_posts
import pandas as pd
from spacy.lang.en import English
import time
import datetime
import json
#load data
data=pd.read_csv('t.csv')
length=data.shape
length=length[0]
#for collecting post
def collect_post(x,m):

    storage_post=[]
    for post in get_posts(x, pages=m):
        tem_post=[]
        Text=post['text'][:500]
        tem_post.append(Text)
        Image=post['image']
        tem_post.append(Image)
        Time=post['time']
        post_id=post['post_id']
        tem_post.append(post_id)
        s=''+str(Time)
        Time_mil=time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S").timetuple())
        tem_post.append(Time_mil)
        storage_post.append(tem_post)
    return storage_post

#print(collect_post(1,2))
a=collect_post(1,2)

def word_split(text):

    # Load English tokenizer, tagger, parser, NER and word vectors
    nlp = English()

    #  "nlp" Object is used to create documents with linguistic annotations.
    my_doc = nlp(text)

    # Create list of word tokens
    token_list = []
    for token in my_doc:
        token_list.append(token.text)
    return token_list

def sorting_by_offer(fb_post):
    intend=['offer','delicious','Tasty','tasty','Offer','OFFER','offers','Offers','OFFERS','Buy','BUY','buy','One','ONE','GET','get','Get','one','Discount','discount','DISCOUNT','Surprise','surprise','Challenge','Exclusive','challenge','%','off','OFF']
    j=0
    post_all=[]
    while j<=2:
        Split=word_split(fb_post[j][0])
        i=0
        c=0
        while True:
            if intend[i] in Split:
                c=c+1
            i=i+1
            if i==len(intend):
                break
        if c>=1:
            post_all.append(fb_post[j])
        j=j+1
        #count=count+1
    return post_all







count=1
Data=0
length=149
Data={}
Data['restaurent'] = []
while count<=length:
    t=0
    x=data['name']
    x=x[count]
    print(x)
    try:
        a=collect_post(x,4)
        f=sorting_by_offer(a)
        if len(f)>=1:
            while t<=len(f)-1:
                pst=f[t][0]
                pht=f[t][1]
                pst_id=f[t][2]
                tm=f[t][3]
                t=t+1
                Data['restaurent'].append({
                'name': ''+str(x),
                'website_photo':pht,
                'pst_id':pst_id,
                'post':''+str(pst),
                'time':tm
                })
        else:
            None
    except:
        None
    count=count+1
    print(count)
print(Data)
with open('data.txt', 'w') as outfile:
    json.dump(Data, outfile)