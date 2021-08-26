# Illustration-of-Data-Processing-and-Preparation-with-Python-Libraries
In this tutorial, we use the Titanic Data (obtained from Kaggle) to illustrate key aspects of Data Processing and Preparation
To complete this exercise, there is relying on useful Python Libraries

First, there is need to import numpy and pandas, and then import the dataset for using

<code>
<pre>
        import numpy as np
        import pandas as pd

          TitanicData = pd.read_csv('D:/github/Python/train.csv')      # In this section, one replaces their specific path to read the data
          TitanicData.head()                                          # To visualize the data, the .head() is used to view the first five elements
</pre>
</code>
The image below shows the dataset's outlook
<img src="https://github.com/danny-votez/Illustration-of-Data-Processing-and-Preparation-with-Python-Libraries/blob/main/datasetview.jpg">

Next, we can get more information about the Titanic data, using the info() tool, which will be coded as;
<code>
<pre>
    TitanicData.info()                                  # Gives a summarized information about our dataset
</pre>
</code>

As shown, the info gives the data types of the respective columns and number of entries.
Based on this representation, it is evident some columns have missing items, that can be examined later

<img src="https://github.com/danny-votez/Illustration-of-Data-Processing-and-Preparation-with-Python-Libraries/blob/main/datasetinfo.jpg">
