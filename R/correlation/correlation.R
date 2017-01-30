

library(caret) 
library(RCurl) 
library(Metrics) 
library(xgboost) 


#Let us load the data for the further processing.

urlfile <- 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'
x <- getURL(urlfile, ssl.verifypeer = FALSE)
adults <- read.csv(textConnection(x), header=F)

names(adults)

names(adults)<- c('Age','Workclass','FinalWeight','Education','EducationNumber',
                'MaritalStatus','Occupation','Relationship','Race',
                'Sex','CapitalGain','CapitalLoss','HoursWeek',
                'NativeCountry','Income')

adults$Income <- ifelse(adults$Income==' <=50K',1,0)

#The correlation work for numerical values only.
#So first we have to convert the categorical variable into numerical variable using powerful package caret.
#In this package we use dummyVars funcion for coverting the categorical variable.

library(caret)
dmy <- dummyVars(" ~ .", data = adults)
adultsTrsf <- data.frame(predict(dmy, newdata = adults))

#Correlation matrix with p-values

cor.prob <- function (X, dfr = nrow(X) - 2) {
  R <- cor(X, use="pairwise.complete.obs")
  above <- row(R) < col(R)
  r2 <- R[above]^2
  Fstat <- r2 * dfr/(1 - r2)
  R[above] <- 1 - pf(Fstat, 1, dfr)
  R[row(R) == col(R)] <- NA
  R
}

cor.prob(adultsTrsf)

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

corList <- corMasterList[order(-abs(corMasterList$cor)),]

#Sort the matrix by correlation value
corList <- corMasterList[order(corMasterList$cor),]

#Subset those variable which is highly correlated with target variable.
selectedSub <- subset(corList, (abs(cor) > 0.2 & j == 'Income'))
bestSub <-  sapply(strsplit(as.character(selectedSub$i),'[.]'), "[", 1)

library(psych)
pairs.panels(adults[c(bestSub,'Income')])


