import pandas as pd
import numpy as np
import sys
import pickle
from pandas.core.dtypes.missing import isna

topics = sys.argv[1]
queryclass=sys.argv[2]
qrel = sys.argv[3]


#delet colmun and creat new file from original dataset
def edit_trec2009MQ(dataset):
    data = pd.read_csv(f'../ds/trec2009mq/output/{dataset}', encoding ="ISO-8859-1", sep=' ', header=None, index_col=False)
    print(data)
    data=data.drop(data.columns[1],axis=1)
    data.to_csv(r'../ds/trec2009mq/output/topics_trec', header=None, index=None, sep='\t', mode='a')
    #data1 = pd.read_csv(f'topics.trecMQ', encoding = "ISO-8859-1", sep=' ',header=None, index_col=False)

# this is a proof that all queries in queryclass dataset  are exist in topic dataset
def find_query_type(queryclass):
    queryclass = pd.read_csv(f'../ds/trec2009mq/source/{queryclass}', encoding='utf-8', sep='\t')
    #print(queryclass)
    topics= pd.read_csv(f'../qe/output/antique/topics.antique.stem.porter2.bm25.map.txt', encoding = "ISO-8859-1", sep='\t',header=None, index_col=False)
    topics2=pd.read_csv(f'../qe/output/antique/topics.antique.stem.lovins.bm25.map.txt', encoding = "ISO-8859-1", sep='\t',header=None, index_col=False)
    print(queryclass["Class"][1])
    print( topics[1][1])

    for i in range(len(topics)):
        for j in range(len(queryclass)):
            if str(queryclass["Topic"][j]) == str(topics[1][i]):
                if str(queryclass["Class"][j])== "Information_Close":
                    print((queryclass.loc[j]))
                    #print(topics.loc[i])
                    (topics.loc[[i]]).to_csv(r'../preprocess_trec2009/output/informational_close_prter', header=None, index=None, sep=' ',mode='a')
                elif str(queryclass["Class"][j])== "Information_Open":
                    #print(topics.loc[i])
                    (topics.loc[[i]]).to_csv(r'../preprocess_trec2009/output/Information_Open_prter', header=None, index=None, sep=' ',mode='a')
                elif str(queryclass["Class"][j]) == "Navigational":
                    # print(topics.loc[i])
                    (topics.loc[[i]]).to_csv(r'../preprocess_trec2009/output/Navigational_prter', header=None,index=None, sep=' ', mode='a')
                elif str(queryclass["Class"][j]) == "Resource":
                    # print(topics.loc[i])
                    (topics.loc[[i]]).to_csv(r'../preprocess_trec2009/output/Resource_prter', header=None,index=None, sep=' ', mode='a')
                elif str(queryclass["Class"][j]) == "Advice":
                    # print(topics.loc[i])
                    (topics.loc[[i]]).to_csv(r'../preprocess_trec2009/output/Advice_prter', header=None, index=None,sep=' ', mode='a')
    for i in range(len(topics)):
        for j in range(len(queryclass)):
            if str(queryclass["Topic"][j]) == str(topics[1][i]):
                if str(queryclass["Class"][j]) == "Information_Close":
                    (topics.loc[[i]]).to_csv(r'../preprocess_trec2009/output/informational_close_lovins',
                                                         header=None, index=None, sep=' ', mode='a')
                elif str(queryclass["Class"][j]) == "Information_Open":
                                # print(topics.loc[i])
                    (topics.loc[[i]]).to_csv(r'../preprocess_trec2009/output/Information_Open_lovins',
                                                         header=None, index=None, sep=' ', mode='a')
                elif str(queryclass["Class"][j]) == "Navigational":
                                # print(topics.loc[i])
                     (topics.loc[[i]]).to_csv(r'../preprocess_trec2009/output/Navigational_lovins',
                                                         header=None, index=None, sep=' ', mode='a')
                elif str(queryclass["Class"][j]) == "Resource":
                                # print(topics.loc[i])
                     (topics.loc[[i]]).to_csv(r'../preprocess_trec2009/output/Resource_lovins', header=None,
                                                         index=None, sep=' ', mode='a')
                elif str(queryclass["Class"][j]) == "Advice":
                                # print(topics.loc[i])
                     (topics.loc[[i]]).to_csv(r'../preprocess_trec2009/output/Advice_lovins', header=None,
                                                         index=None, sep=' ', mode='a')

                #(topics.loc[[i]]).to_csv(r'../ds/trec2009mq/output/queryclass_topics', header=None, index=None, sep=' ',mode='a')
                #(queryclass.loc[[j]]).to_csv(r'../ds/trec2009mq/output/final_types', header=None, index=None, sep=' ',mode='a')


#        data1 = pd.read_csv(f'../ds/trec2009mq/output/rv_09.mq.topics.20001-60000', encoding="ISO-8859-1", sep=' ', header=None, index_col=False)
#        data2 = pd.read_csv(f'../ds/trec2009mq/output/final_types', encoding="ISO-8859-1", sep=' ', header=None, index_col=False)
       # print(len(data1),len(queryclass))

        #(data.loc[[i]]).to_csv(r'final_queries', header=None, index=None, sep=' ', mode='a')
       # print(queryclass.loc[[i]])
    #data1 = pd.read_csv(f'final_queries', sep=' ', header=None, index_col=False)
    #print(queryclass["Topic"][0])

    #data.to_csv(r'topics.trecMQ', header=None, index=None, sep=' ', mode='a')


#data1 = pd.read_csv(f'ds/trec2009mq/output/rv_09.mq.topics.20001-60000', encoding = "ISO-8859-1", sep=' ',header=None, index_col=False)
#print(data1)
def qrel():
    qrel = pd.read_csv(f'../ds/trec2009mq/source/prels.20001-60000', encoding='utf-8', sep=' ')

    data = qrel.drop(qrel.columns[3], axis=1)
    data = data.drop(data.columns[3], axis=1)
    #data = qrel.join(qrel.columns[3], axis=1)
    data["d"] = 0
    data.to_csv(r'rev_qrel_trec', header=["a","b","c","d"], index=None, sep=' ', mode='a')

   # data.to_csv(r'rev_qrel_trec1', header=["a", "b", "c","d"], index=None, sep=' ', mode='a')
    #rv_qrel = pd.read_csv(f'rev_qrel_trec', encoding='utf-8', sep=' ')
    #rv_qrel1 = pd.read_csv(f'rev_qrel_trec1', encoding='utf-8', sep=' ')




def swap_columns(df, col1, col2):
        col_list = list(df.columns)
        x, y = col_list.index(col1), col_list.index(col2)
        col_list[y], col_list[x] = col_list[x], col_list[y]
        df = df[col_list]
        return df

    # swap points and rebounds columns

#categorized query classes into different files
def query_class():
    classes = pd.read_csv(f'../ds/trec2009mq/source/queryclasses', encoding='utf-8', sep='\t')
    topics = pd.read_csv(f'../ds/trec2009mq/output/topics_trec', encoding="ISO-8859-1", sep='\t', header=None, index_col=False)
    for i in range(len(classes)):
        for j in range(len(classes)):
            if str(classes["Topic"][i]) == str(topics[0][j]):
                if str(classes["Class"][i]) == "Information_Close":
                    print((topics.loc[i]))
                    # print(topics.loc[i])
                    (topics.loc[[i]]).to_csv(r'../ds/trec2009mq/output/topics_trec_Information_Close', header=None, index=None, sep='\t', mode='a')
                elif str(classes["Class"][i])== "Information_Open":
                    #print(topics.loc[i])
                    (topics.loc[[i]]).to_csv(r'../ds/trec2009mq/output/topics_trec_Information_Open', header=None, index=None, sep='\t',mode='a')
                elif str(classes["Class"][i]) == "Navigational":
                    # print(topics.loc[i])
                    (topics.loc[[i]]).to_csv(r'../ds/trec2009mq/output/topics_trec_Navigational', header=None,index=None, sep='\t', mode='a')
                elif str(classes["Class"][i]) == "Resource":
                    # print(topics.loc[i])
                    (topics.loc[[i]]).to_csv(r'../ds/trec2009mq/output/topics_trec_Resource', header=None,index=None, sep='\t', mode='a')
                elif str(classes["Class"][i]) == "Advice":
                    # print(topics.loc[i])
                    (topics.loc[[i]]).to_csv(r'../ds/trec2009mq/output/topics_trec_Advice', header=None, index=None,sep='\t', mode='a')
             # print(topics)


if __name__ == "__main__":
   #find_query_type(queryclass)
   #dsquery_class()
   #topics = pd.read_csv(r'../preprocess_trec2009/output/Information_Open_prter', encoding="ISO-8859-1",sep='\t', header=None, index_col=False)
   #print(len(topics))
   edit_trec2009MQ("queryclass_topics")
   qrel()
   rv_qrel1 = pd.read_csv(f'rev_qrel_trec', encoding='utf-8', sep=' ')
   #///////////
   df = swap_columns(rv_qrel1, 'd', 'b')
   df = swap_columns(df, 'c', 'b')
   df.to_csv(r'../ds/trec2009mq/output/qrels_trec', header=None, index=None, sep=' ', mode='a')
   #rv_qrel2 = pd.read_csv(f'../ds/trec2009mq/output/qrels_trec', encoding='utf-8', sep=' ')

   # view updated DataFrame
   #print(rv_qrel2)



