import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from application_logging import logger


class visualization_graph:
    """
    This class shall  be used for Visualization of data


    """

    def __init__(self):

        self.log_writer = logger.App_Logger()
        self.file_object = open("Visualization_Logs/VisualizationLog.txt", 'a+')

    def visualize_accuracy(self, data, cluster_number):
        """
        Method Name: visualize_accuracy
        Description: This method visualizes the Accuracy of models
        Output: A png file.
        On Failure: Raise Exception


        """
        self.log_writer.log(self.file_object, 'Entered the visualize_accuracy method of the Visualization class')
        try:
            df  = pd.DataFrame(data.items(), columns=['Model', 'Accuracy'])
            ax = sns.barplot(x='Model', y='Accuracy', data=df)
            ax.bar_label(ax.containers[0])
            plt.xlabel("Models")
            plt.ylabel("Accuracies")

            # Saving figure by changing parameter values
            plt.savefig("Visualizations/accuracy_graph_cluster_" + str(cluster_number) + ".png", bbox_inches="tight",
                        pad_inches=0.3)
            plt.close()
            self.log_writer.log(self.file_object,
                                'Data Load Successful.Exited the visualize_accuracy method of the Visualization class')
        except Exception as e:
            self.log_writer.log(self.file_object,
                                'Exception occured in visualize_accuracy method of the Visualization class. Exception message: ' + str(
                                    e))
            self.log_writer.log(self.file_object,
                                'Data Load Unsuccessful.Exited the visualize_accuracy method of the Visualization class')
            raise Exception()
