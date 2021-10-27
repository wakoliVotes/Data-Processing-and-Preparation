### Illustrating Data Processing and Preparation with Python Libraries
- In this tutorial, we use the Titanic Data (obtained from Kaggle) to illustrate key aspects of Data Processing and Preparation
- To complete this exercise, there is relying on useful Python Libraries

- First, there is need to import numpy and pandas, and then import the dataset for using

<code>
<pre>
        import numpy as np
        import pandas as pd

          TitanicData = pd.read_csv('D:/github/Python/train.csv')  # In this section, one replaces their specific path to read the data
          TitanicData.head()                              # To visualize the data, the .head() is used to view the first five elements
</pre>
</code>
The image below shows the dataset's outlook
<img src="https://github.com/danny-votez/Illustration-of-Data-Processing-and-Preparation-with-Python-Libraries/blob/main/datasetview.jpg">

As seen from above, the head() keyword gives the first 5 elements. However, if you want to get a specific number of items, you can adjust by adding "n="number of rows you need"". 
This is illustrated below, where, to show 10 items, inside the head() function, n=10 is added, to specify the desired rows of data to show;

<pre>
          import numpy as np
          import pandas as pd
          
          TitanicData = pd.read_csv('D:/github/Python/train.csv')
          
          # To get varied display rows, specify the value using the n item, e.g., n=8, or n=10, or n=30
          
          TitanicData.head(n=10)                        # Gives 10 rows of dataset
</pre>
The below image shows the visualization with 10 rows;

![image](https://user-images.githubusercontent.com/77758884/130964763-26eef94b-93e8-4ceb-923a-981f7e590484.png)


Next, we can get more information about the Titanic data, using the info() tool, which will be coded as;
<code>
<pre>
    TitanicData.info()                                  # Gives a summarized information about our dataset
</pre>
</code>

As shown, the info gives the data types of the respective columns and number of entries.
Based on this representation, it is evident some columns have missing items, that can be examined later

<img src="https://github.com/danny-votez/Illustration-of-Data-Processing-and-Preparation-with-Python-Libraries/blob/main/datasetinfo.jpg">

We can use the describe function to get additional information on the dataset, including its mean, mode, standard deviation, percentiles, etc. This is achieved with the code below {remember to replace the file name, i.e., TitanicData, with your respective data file name}

<code>
<pre>
                TitanicData.describe()   # Gives additional descriptive statistics information about our dataset
</pre>
</code>
Below is the describe output for the used dataset

![image](https://user-images.githubusercontent.com/77758884/130960566-77c5685f-e2a0-4c46-8d3a-74a6dd42fd5b.png)


As shown from above, we can see that for the TitanicData, basic descriptive statistics can help us understand the data more.
For example, from the data, the mean values are evident. In the sample, we can see the means of;
<pre>
        - Passengers, i.e., PassengerId (446.00),
        - Survived (0.383838),
        - Pclass (2.308642),
        - Age (29.699118),
        - SibSp (0.523008),
        - Parch (0.381594) and,
        - Fare (32.204208).
</pre>
NOTE: The above describe() function only gives columns that have continuous data elements, while there is excluding caterorical data.
However, if you need to include everything, you can add the "(include='all')" after writing the describe() function.
This is as illustrated below;
<pre>
            TitanicData.describe(include='all')        # Gives descriptive statistics for all columns
</pre>
Below is now the outlook for all columns in the dataset;
![image](https://user-images.githubusercontent.com/77758884/130963069-7c442688-764b-4ee1-aa00-778bc5f6ff75.png)



