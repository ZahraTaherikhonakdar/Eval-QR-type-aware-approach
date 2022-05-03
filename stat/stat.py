import numpy as np
import pandas as pd
import csv
import seaborn as sns
import matplotlib.pyplot as plt

def bulding_matrix():
    data = pd.read_csv("../qe/output/trec2009mq/topics.antique.bm25.map.dataset.csv")
    classes = pd.read_csv(f'../ds/trec2009mq/source/queryclasses', encoding='utf-8', sep='\t')
    i = 0
    row = 5
    col = 3

    matrix = [[0 for x in range(col)] for y in range(row)]

    for q in range(len(data)):
        for c in range(len(classes)):
            if str(data['qid'][q]) == str(classes["Topic"][c]):
                # row 0 is Information_Close type
                if str(classes["Class"][c]) == "Information_Close":
                    if data["star_model_count"][q] == 1:
                        if str(data["method.1"][q]) == "tagmee.topn3":
                            matrix[0][0] = matrix[0][0] + int(data["star_model_count"][q])
                        elif str(data["method.1"][q]) == "glove.topn3.replace":
                            matrix[0][1] = matrix[0][1] + int(data["star_model_count"][q])
                        elif str(data["method.1"][q]) == "stem.lovins":
                            matrix[0][2] = matrix[0][2] + int(data["star_model_count"][q])
                    elif data["star_model_count"][q] == 2:
                        if str(data["method.1"][q]) == "tagmee.topn3":
                            matrix[0][0] = matrix[0][0] + 1
                        elif str(data["method.1"][q]) == "glove.topn3.replace":
                            matrix[0][1] = matrix[0][1] + 1
                        elif str(data["method.1"][q]) == "stem.lovins":
                            matrix[0][2] = matrix[0][2] + 1
                        if str(data["method.2"][q]) == "tagmee.topn3":
                            matrix[0][0] = matrix[0][0] + 1
                        elif str(data["method.2"][q]) == "glove.topn3.replace":
                            matrix[0][1] = matrix[0][1] + 1
                        elif str(data["method.2"][q]) == "stem.lovins":
                            matrix[0][2] = matrix[0][2] + 1
                # row 1 is Information_Open type
                elif str(classes["Class"][c]) == "Information_Open":
                    if data["star_model_count"][q] == 1:
                        if str(data["method.1"][q]) == "tagmee.topn3":
                            matrix[1][0] = matrix[1][0] + int(data["star_model_count"][q])
                        elif str(data["method.1"][q]) == "glove.topn3.replace":
                            matrix[1][1] = matrix[1][1] + int(data["star_model_count"][q])
                        elif str(data["method.1"][q]) == "stem.lovins":
                            matrix[1][2] = matrix[1][2] + int(data["star_model_count"][q])
                    elif data["star_model_count"][q] == 2:
                        if str(data["method.1"][q]) == "tagmee.topn3":
                            matrix[1][0] = matrix[1][0] + 1
                        elif str(data["method.1"][q]) == "glove.topn3.replace":
                            matrix[1][1] = matrix[1][1] + 1
                        elif str(data["method.1"][q]) == "stem.lovins":
                            matrix[1][2] = matrix[1][2] + 1
                        if str(data["method.2"][q]) == "tagmee.topn3":
                            matrix[1][0] = matrix[1][0] + 1
                        elif str(data["method.2"][q]) == "glove.topn3.replace":
                            matrix[1][1] = matrix[1][1] + 1
                        elif str(data["method.2"][q]) == "stem.lovins":
                            matrix[1][2] = matrix[1][2] + 1
                # row 2 is Navigational type
                elif str(classes["Class"][c]) == "Navigational":
                    if data["star_model_count"][q] == 1:
                        if str(data["method.1"][q]) == "tagmee.topn3":
                            matrix[2][0] = matrix[2][0] + int(data["star_model_count"][q])
                        elif str(data["method.1"][q]) == "glove.topn3.replace":
                            matrix[2][1] = matrix[2][1] + int(data["star_model_count"][q])
                        elif str(data["method.1"][q]) == "stem.lovins":
                            matrix[2][2] = matrix[2][2] + int(data["star_model_count"][q])
                    elif data["star_model_count"][q] == 2:
                        print("hello")
                        if str(data["method.1"][q]) == "tagmee.topn3":
                            matrix[2][0] = matrix[2][0] + 1
                        elif str(data["method.1"][q]) == "glove.topn3.replace":
                            matrix[2][1] = matrix[2][1] + 1
                        elif str(data["method.1"][q]) == "stem.lovins":
                            matrix[2][2] = matrix[2][2] + 1
                        if str(data["method.2"][q]) == "tagmee.topn3":
                            matrix[2][0] = matrix[2][0] + 1
                        elif str(data["method.2"][q]) == "glove.topn3.replace":
                            matrix[2][1] = matrix[2][1] + 1
                        elif str(data["method.2"][q]) == "stem.lovins":
                            matrix[2][2] = matrix[2][2] + 1
                # row 3 is Resource type
                elif str(classes["Class"][c]) == "Resource":
                    if data["star_model_count"][q] == 1:
                        if str(data["method.1"][q]) == "tagmee.topn3":
                            matrix[3][0] = matrix[3][0] + int(data["star_model_count"][q])
                        elif str(data["method.1"][q]) == "glove.topn3.replace":
                            matrix[3][1] = matrix[3][1] + int(data["star_model_count"][q])
                        elif str(data["method.1"][q]) == "stem.lovins":
                            matrix[3][2] = matrix[3][2] + int(data["star_model_count"][q])
                    elif data["star_model_count"][q] == 2:
                        print("hello")
                        if str(data["method.1"][q]) == "tagmee.topn3":
                            matrix[3][0] = matrix[3][0] + 1
                        elif str(data["method.1"][q]) == "glove.topn3.replace":
                            matrix[3][1] = matrix[3][1] + 1
                        elif str(data["method.1"][q]) == "stem.lovins":
                            matrix[3][2] = matrix[3][2] + 1
                        if str(data["method.2"][q]) == "tagmee.topn3":
                            matrix[3][0] = matrix[3][0] + 1
                        elif str(data["method.2"][q]) == "glove.topn3.replace":
                            matrix[3][1] = matrix[3][1] + 1
                        elif str(data["method.2"][q]) == "stem.lovins":
                            matrix[3][2] = matrix[3][2] + 1
                # row 3 is Advice type
                elif str(classes["Class"][c]) == "Advice":

                    if data["star_model_count"][q] == 1:
                        if str(data["method.1"][q]) == "tagmee.topn3":
                            matrix[4][0] = matrix[4][0] + int(data["star_model_count"][q])
                        elif str(data["method.1"][q]) == "glove.topn3.replace":
                            matrix[4][1] = matrix[4][1] + int(data["star_model_count"][q])
                        elif str(data["method.1"][q]) == "stem.lovins":
                            matrix[4][2] = matrix[4][2] + int(data["star_model_count"][q])
                    elif data["star_model_count"][q] == 2:
                        print("hello")
                        if str(data["method.1"][q]) == "tagmee.topn3":
                            matrix[4][0] = matrix[4][0] + 1
                        elif str(data["method.1"][q]) == "glove.topn3.replace":
                            matrix[4][1] = matrix[4][1] + 1
                        elif str(data["method.1"][q]) == "stem.lovins":
                            matrix[4][2] = matrix[4][2] + 1
                        if str(data["method.2"][q]) == "tagmee.topn3":
                            matrix[4][0] = matrix[4][0] + 1
                        elif str(data["method.2"][q]) == "glove.topn3.replace":
                            matrix[4][1] = matrix[4][1] + 1
                        elif str(data["method.2"][q]) == "stem.lovins":
                            matrix[4][2] = matrix[4][2] + 1

    print(matrix)

    with open("../qe/output/trec2009mq/stat/matrix_result.csv", "w") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(matrix)

def heatmap():
    CSVData = open("../qe/output/trec2009mq/stat/matrix_result.csv")
    matrix_result = np.loadtxt(CSVData, delimiter=",")
    x_axis_labels = ["Tagmee", "Glove", "Lovins"]  # labels for x-axis
    y_axis_labels = ["Info_Close", "Info_Open", "Navigational", "Resource", "Advice"]  # labels for y-axis

    # create seabvorn heatmap with required labels
    sns.heatmap(matrix_result, xticklabels=x_axis_labels, yticklabels=y_axis_labels)

    # plt.pcolormesh( Array2d_result, cmap = 'coolwarm')
    plt.title("Improvement of the initial queries \n by different query expanders given a query type.", fontsize=12)

    plt.savefig("../qe/output/trec2009mq/stat/heatmap.png", bbox_inches='tight', dpi=100)

    plt.show()
if __name__ == "__main__":

    bulding_matrix()
    heatmap()


