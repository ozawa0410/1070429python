
# coding: utf-8

# In[1]:


import pandas as pd

dfs = pd.read_csv("ted_main.csv", encoding = "utf-8")
dfs


# In[2]:


dfs.shape


# In[3]:


dfs.shape[0]


# In[4]:


dfs_t = dfs.T
dfs_t


# In[5]:


dfs_t.to_csv("ted_main_transform.csv", encoding = "utf-8")


# In[6]:


dfs["comments"]


# In[7]:


dfs[ ["comments", "description", "duration"] ]


# In[8]:


del dfs['num_speaker']
dfs


# dfs.iloc -> ["第一筆資料", "第二筆資料", "第三筆資料"]

# In[9]:


dfs.iloc[0]


# In[10]:


dfs.iloc[0:10]


# dfs.head(10)
# 

# In[11]:



































dfs.head(10)


# In[12]:


dfs.tail(10)


# In[13]:


dfs.iloc[999:]


# In[14]:


dfs.iloc[:]


# In[15]:


dfs[ ['comments', 'description'] ].iloc[999:]


# dfs.[_特別東西_]. 特別東西 -> .[True,False,.....]. (他的個數必須跟dataframe的資料筆數依樣多)
# dfs -> 假設五筆資料 dfs.[_[True,False, True, True, False ]. ]
# _

# In[16]:


.dfs['description'].str.contains["Sir"]


# In[ ]:


fil = dfs['description'].str.contains("Sir")
fil


# In[ ]:


dfs[fil]


# In[ ]:


dfs[fil].shape


# In[ ]:


dfs[dfs['description'].str.contains(r"\bSir\b")]


# #### dfs[dfs['description'].str.contains(r"\bSir\b")].shape
# 

# 複雜的篩選 -> (一行).apply(技能) 技能 最後一定要 return True or False
# eval -> 你傳給他的字串 他會當python程式執行

# In[ ]:


eval("print('hello')")


# In[ ]:


def flow(in_data):
    a = eval(in_data)
    result = 'children' in a
    return result
fil = dfs['tags'].apply(flow)
fil 


# In[ ]:


dfs[fil]

