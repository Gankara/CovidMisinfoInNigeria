#!/usr/bin/env python
# coding: utf-8

# In[1]:
from searchtweets import load_credentials


premium_search_args = load_credentials("apicred.yaml",
                                       yaml_key="search_tweets_api",
                                       env_overwrite=False)

print(premium_search_args)


# In[18]:


from searchtweets import gen_rule_payload 

# query = "(covid OR covid19)"
# query = "CovidNigeria"

query = "Covid-19 lang:en place_country:NG"

rule = gen_rule_payload(query, results_per_call=500, from_date="2020-01-01", to_date="2020-10-31")

print(rule)


# In[19]:


from searchtweets import ResultStream

rs = ResultStream(rule_payload=rule,
                  max_results=100000,
                  **premium_search_args)
print(rs)


# In[20]:


import json

with open('data/json/c2_ng.jsonl', 'a', encoding='utf-8') as f:
    for tweet in rs.stream():
        json.dump(tweet, f)
        f.write('\n')
        
print('done')


# In[ ]:




