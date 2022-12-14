# ShoeColor

**Goal**
---
>Extracting the colors of <b>1000 shoes</b> into <b>25 colors</b>

>Practice writing [Markdown](https://en.wikipedia.org/wiki/Markdown) through [Jupyter notebook](https://en.wikipedia.org/wiki/Project_Jupyter), extracting data from websites and visualizing by using [matplotlib](https://matplotlib.org/).

<br>

**contents**
---
* [Get Product Infromation](/data_crawl/GetProducts.ipynb)
  #### Web Scraping using Beautiful Soup and Selenium
  <br>
* [Color Clustering](/color/ColorClustering.ipynb)
  #### Extraction of 25 colors using K-Means Clustering
    * [Get Color Name](/data_crawl/GetColorName.ipynb)
      #### Get Name of Color using artyclick color name
    * [Approximate Clustering](/color/ApproximateClustering.ipynb)
      #### Get 25 distant colors using the Greedy method
  <br>
* [Shoes Number](/graph/shoesNumber.ipynb)
  #### Number of shoes according to 25 extracted colors
  <br>


**Results**
---
25 colors extracted and the number of shoes according to them

![ColorCluster2d](https://user-images.githubusercontent.com/67538999/206905496-a04a1cb6-1434-4a0c-b55c-dd70cd146e50.png)
![numsofshoes](https://user-images.githubusercontent.com/67538999/206905415-986dd66b-c29c-447c-ad4e-51161fe05ba7.png)

<br>

**Requirement**
---
* [numpy](https://numpy.org/)
* [pandas](https://pandas.pydata.org/)
* [matplotlib](https://matplotlib.org/)
* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
* [selenium](https://selenium-python.readthedocs.io/)
* [colorthief](https://pypi.org/project/colorthief/)

**Reference**
---
- sort by color's rgb value
  https://www.alanzucconi.com/2015/09/30/colour-sorting/
- get ratio of colors in color-thief 
  https://github.com/fengsp/color-thief-py/issues/1

