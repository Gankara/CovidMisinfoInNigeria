#!/usr/bin/env python
# coding: utf-8

# In[36]:


import json
# import time
import pandas as pd


# import sys

def to_csv(json_filename, tsv_filename):
    fO = open(tsv_filename, "w")

    with open(json_filename, 'r') as f:
        cnt = 1

        for cnt, line in enumerate(f):
            try:
                tweet = json.loads(line)  # load it as Python dict
            except:
                continue
            try:
                tweet_created_at = str(tweet["created_at"])
            except:
                tweet_created_at = 'NULL'
            try:
                tweet_id = str(tweet["id"])
            except:
                tweet_id = 'NULL'
            try:
                tweet_text = str(tweet["text"])
            except:
                tweet_text = 'NULL'
            try:
                tweet_truncated = str(tweet["truncated"])
            except:
                tweet_truncated = 'NULL'
            try:
                tweet_source = str(tweet["source"])
            except:
                tweet_source = 'NULL'
            try:
                tweet_in_reply_to_status_id = str(tweet["in_reply_to_status_id"])
            except:
                tweet_in_reply_to_status_id = 'NULL'
            try:
                tweet_in_reply_to_user_id = str(tweet["in_reply_to_user_id"])
            except:
                tweet_in_reply_to_user_id = 'NULL'
            try:
                tweet_in_reply_to_screen_name = str(tweet["in_reply_to_screen_name"])
            except:
                tweet_in_reply_to_screen_name = 'NULL'
            try:
                tweet_coordinates = str(tweet["coordinates"])
            except:
                tweet_coordinates = 'NULL'
            try:
                tweet_place = str(tweet["place"])
            except:
                tweet_place = 'NULL'
            try:
                tweet_user = str(tweet["user"])
            except:
                tweet_user = 'NULL'
            try:
                tweet_lang = str(tweet["lang"])
            except:
                tweet_lang = 'NULL'
            try:
                tweet_full_text = str(tweet["extended_tweet"]["full_text"])
            except:
                tweet_full_text = 'NULL'
            try:
                tweet_entities = str(tweet["entities"])
            except:
                tweet_entities = 'NULL'
            try:
                tweet_is_quote_status = str(tweet["is_quote_status"])
            except:
                tweet_is_quote_status = 'NULL'
            try:
                tweet_quoted_status_id = str(tweet["quoted_status_id"])
            except:
                tweet_quoted_status_id = 'NULL'
            try:
                tweet_retweeted_status = str(tweet["retweeted_status"])
            except:
                tweet_retweeted_status = 'NULL'
            try:
                tweet_favorited = str(tweet["favorited"])
            except:
                tweet_favorited = 'NULL'
            try:
                tweet_retweeted = str(tweet["retweeted"])
            except:
                tweet_retweeted = 'NULL'
            try:
                tweet_possibly_sensitive = str(tweet["possibly_sensitive"])
            except:
                tweet_possibly_sensitive = 'NULL'

            objectString = (tweet_created_at + "\t" +
                            tweet_id + "\t" +
                            tweet_text + "\t" +
                            tweet_truncated + "\t" +
                            tweet_source + "\t" +
                            tweet_in_reply_to_status_id + "\t" +
                            tweet_in_reply_to_user_id + "\t" +
                            tweet_in_reply_to_screen_name + "\t" +
                            tweet_coordinates + "\t" +
                            tweet_place + "\t" +
                            tweet_user + "\t" +
                            tweet_full_text + "\t" +
                            tweet_entities + "\t" +
                            tweet_lang + "\t" +
                            tweet_is_quote_status + "\t" +
                            tweet_quoted_status_id + "\t" +
                            tweet_retweeted_status + "\t" +
                            tweet_favorited + "\t" +
                            tweet_retweeted + "\t" +
                            tweet_possibly_sensitive)
            objectString = objectString.replace('\n', '')
            objectString = objectString.replace('\r', '')
            fO.write(objectString + "\n")
            cnt += 1


# In[37]:


to_csv('data/json/aa_ng.jsonl', 'data/tsv/aa_ng.tsv')

# In[38]:


res = pd.read_csv('data/tsv/aa_ng.tsv', sep='\t', error_bad_lines=False, header=None)
res.columns = ['tweet_created_at',
               'tweet_id',
               'tweet_text',
               'tweet_truncated',
               'tweet_source',
               'tweet_in_reply_to_status_id',
               'tweet_in_reply_to_user_id',
               'tweet_in_reply_to_screen_name',
               'tweet_coordinates',
               'tweet_place',
               'tweet_user',
               'tweet_full_text',
               'tweet_entities',
               'tweet_lang',
               'tweet_is_quote_status',
               'tweet_is_quote_status_id',
               'tweet_retweeted_status',
               'tweet_favorited',
               'tweet_retweeted',
               'tweet_possibly_sensitive']

# In[ ]:


# In[ ]:
