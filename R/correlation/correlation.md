Correlation using R
================

Loading Data
------------

Let us load the data for the further processing.

``` r
library(RCurl)
```

    ## Loading required package: bitops

``` r
urlfile <- 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'
x <- getURL(urlfile, ssl.verifypeer = FALSE)
adults <- read.csv(textConnection(x), header=F)

names(adults)
```

    ##  [1] "V1"  "V2"  "V3"  "V4"  "V5"  "V6"  "V7"  "V8"  "V9"  "V10" "V11"
    ## [12] "V12" "V13" "V14" "V15"

``` r
names(adults)<- c('Age','Workclass','FinalWeight','Education','EducationNumber',
                'MaritalStatus','Occupation','Relationship','Race',
                'Sex','CapitalGain','CapitalLoss','HoursWeek',
                'NativeCountry','Income')

adults$Income <- ifelse(adults$Income==' <=50K',1,0)
```

Convert Categorical Variable into Numerical
-------------------------------------------

The correlation work for numerical values only. So first we have to convert the categorical variable into numerical variable using powerful package **caret**. In this package we use **dummyVars** funcion for coverting the categorical variable.

``` r
library(caret)
```

    ## Loading required package: lattice

    ## Loading required package: ggplot2

``` r
dmy <- dummyVars(" ~ .", data = adults)
adultsTrsf <- data.frame(predict(dmy, newdata = adults))
```

Correlation matrix with p-values
--------------------------------

Then define **cor.prob** which give the correlation matrix with p-values.

``` r
cor.prob <- function (X, dfr = nrow(X) - 2) {
  R <- cor(X, use="pairwise.complete.obs")
  above <- row(R) < col(R)
  r2 <- R[above]^2
  Fstat <- r2 * dfr/(1 - r2)
  R[above] <- 1 - pf(Fstat, 1, dfr)
  R[row(R) == col(R)] <- NA
  R
}
```

Use this cor.prob output to a 4 column matrix with row/column indices, correlation, and p-value.

``` r
flattenSquareMatrix <- function(m) {
  if( (class(m) != "matrix") | (nrow(m) != ncol(m))) stop("Must be a square matrix.")
  if(!identical(rownames(m), colnames(m))) stop("Row and column names must be equal.")
  ut <- upper.tri(m)
  data.frame(i = rownames(m)[row(m)[ut]],
             j = rownames(m)[col(m)[ut]],
             cor=t(m)[ut],
             p=m[ut])
}

corMasterList <- flattenSquareMatrix (cor.prob(adultsTrsf))
print(head(corMasterList,10))
```

    ##                         i                       j          cor
    ## 1                     Age            Workclass...  0.042627419
    ## 2                     Age  Workclass..Federal.gov  0.051226824
    ## 3            Workclass...  Workclass..Federal.gov -0.042606474
    ## 4                     Age    Workclass..Local.gov  0.060900673
    ## 5            Workclass...    Workclass..Local.gov -0.064069751
    ## 6  Workclass..Federal.gov    Workclass..Local.gov -0.045682288
    ## 7                     Age Workclass..Never.worked -0.019361738
    ## 8            Workclass... Workclass..Never.worked -0.003584571
    ## 9  Workclass..Federal.gov Workclass..Never.worked -0.002555830
    ## 10   Workclass..Local.gov Workclass..Never.worked -0.003843346
    ##               p
    ## 1  1.421085e-14
    ## 2  0.000000e+00
    ## 3  1.454392e-14
    ## 4  0.000000e+00
    ## 5  0.000000e+00
    ## 6  2.220446e-16
    ## 7  4.759221e-04
    ## 8  5.177606e-01
    ## 9  6.446737e-01
    ## 10 4.879990e-01

Choose variable of high correlation
-----------------------------------

Sort the matrix by correlation value

``` r
corList <- corMasterList[order(corMasterList$cor),]
```

Subset those variable which is highly correlated with target variable.

``` r
selectedSub <- subset(corList, (abs(cor) > 0.2 & j == 'Income'))

bestSub <-  sapply(strsplit(as.character(selectedSub$i),'[.]'), "[", 1)
```

Plot the selected variable

``` r
library(psych)
```

    ## 
    ## Attaching package: 'psych'

    ## The following objects are masked from 'package:ggplot2':
    ## 
    ##     %+%, alpha

``` r
pairs.panels(adults[c(bestSub,'Income')])
```

![](correlation_files/figure-markdown_github/unnamed-chunk-7-1.png)
