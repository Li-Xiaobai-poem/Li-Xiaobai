
import re
import random
import pandas as pd
import numpy as np
from keras.preprocessing import sequence
from keras.optimizers import SGD, RMSprop, Adagrad
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM, GRU

# In[2]:


'''
@author 邓钧恒
@date 2021/07/09
读取数据, 生成汉字列表
'''
with open('../static/poe/poetry.txt', 'r', encoding='UTF-8') as f:
    raw_text = f.read()
lines = raw_text.split("\n")[:-1]
poem_text = [i.split(':')[1] for i in lines]
char_list = [re.findall('[\x80-\xff]{3}|[\w\W]', s) for s in poem_text]

# In[3]:

'''
@author 邓钧恒
@date 2021/07/09
汉字 <-> 数字 映射
'''
all_words = []
for i in char_list:
    all_words.extend(i)
word_dataframe = pd.DataFrame(pd.Series(all_words).value_counts())
word_dataframe['id'] = list(range(1, len(word_dataframe) + 1))

word_index_dict = word_dataframe['id'].to_dict()
index_dict = {}
for k in word_index_dict:
    index_dict.update({word_index_dict[k]: k})

len(all_words), len(word_dataframe), len(index_dict)

'''
@author 邓钧恒
@date 2021/07/09
生成训练数据, x 为 前两个汉字, y 为 接下来的汉字
'''
seq_len = 1
dataX = []
dataY = []
for i in range(0, len(all_words) - seq_len, 1):
    seq_in = all_words[i: i + seq_len]
    seq_out = all_words[i + seq_len]
    dataX.append([word_index_dict[x] for x in seq_in])
    dataY.append(word_index_dict[seq_out])

len(dataY)

# In[5]:

'''
@author 徐桑儒
@date 2021/07/09
向量转换
'''
X = np.array(dataX)
y = np_utils.to_categorical(np.array(dataY))
X.shape, y.shape

# In[6]:

'''
@author 徐桑儒
@date 2021/07/09
分词
'''
model = Sequential()

'''
@author 徐桑儒
@date 2021/07/09
Embedding 层将正整数（下标）转换为具有固定大小的向量
'''

'''
@author 徐桑儒
@date 2021/07/09
embedding 层只作为模型的第一层
'''

'''
@author 徐桑儒
@date 2021/07/09
 input_dim：大或等于0的整数，字典长度
 output_dim：大于0的整数，代表全连接嵌入的维度
'''

model.add(Embedding(len(word_dataframe), 512))

'''
@author 林绰禧
@date 2021/07/09
LSTM
'''

model.add(LSTM(512))

'''
@author 林绰禧
@date 2021/07/09
 Dropout 防止过拟合
'''

model.add(Dropout(0.5))
'''
@author 林绰禧
@date 2021/07/09
output 为 y 的维度
'''

model.add(Dense(y.shape[1]))

model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

model.summary()

# In[7]:



'''
@author 林绰禧
@date 2021/07/09
训练
'''


model.fit(X, y, batch_size=64, epochs=40)


# In[8]:


def get_predict_array(seed_text):
    chars = re.findall('[\x80-\xff]{3}|[\w\W]', seed_text)
    x = np.array([word_index_dict[k] for k in chars])
    proba = model.predict(x, verbose=0)
    return proba


get_predict_array("明")


# 可以看到预测出来的结果是两个列表, 下一个字是第二个列表


# In[9]:


def gen_poetry(model, seed_text, rows=4, cols=5):
    '''
    生成诗词的函数
    输入: 两个汉字, 行数, 每行的字数 (默认为五言绝句)
    '''
    total_cols = cols + 1  # 加上标点符号
    chars = re.findall('[\x80-\xff]{3}|[\w\W]', seed_text)
    if len(chars) != seq_len:  # seq_len = 1
        return ""
    arr = [word_index_dict[k] for k in chars]
    for i in range(seq_len, rows * total_cols):
        if (i + 1) % total_cols == 0:  # 逗号或句号
            if (i + 1) / total_cols == 2 or (i + 1) / total_cols == 4:  # 句号的情况
                arr.append(2)  # 句号在字典中的映射为 2
            else:
                arr.append(1)  # 逗号在字典中的映射为 1
        else:
            proba = model.predict(np.array(arr[-seq_len:]), verbose=0)
            predicted = np.argsort(proba[1])[-5:]
            index = random.randint(0, len(predicted) - 1)  # 在前五个可能结果里随机取, 避免每次都是同样的结果
            new_char = predicted[index]
            while new_char == 1 or new_char == 2:  # 如果是逗号或句号, 应该重新换一个
                index = random.randint(0, len(predicted) - 1)
                new_char = predicted[index]
            arr.append(new_char)
    poem = [index_dict[i] for i in arr]
    return "".join(poem)

# In[10]:

model.save(filepath='lstm_poetry3.hdf5')