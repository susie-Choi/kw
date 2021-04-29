library(dummies)
library(ggplot2)
install.packages("corrgram")
library(corrgram)

csv2 <- read.csv('../train.csv')
head(csv2)

sum(is.na(csv2))
dim(csv2)

#--전처리--#
#price_range를 range로 이진분류
price <- transform(csv2, range = ifelse(price_range == 0 | price_range == 1, 0, 1))
head(price)
table(price$range)

#EDA
#Bar plot, scatter plot, pie chart, histogram, correlation matrix
corrPrice <- price[,c(12,13,14,18)]
cols <- colorRampPalette(c("blue","skyblue"))
corrgram(corrPrice, col.regions=cols,order=TRUE, lower.panel=panel.fill,upper.panel=panel.pie,
         text.panel=panel.txt,main="Corrgram of Mobile Phone's X variables")

install.packages("ggcorrplot")
library(ggcorrplot)
corr <- round(cor(price), 8)
ggcorrplot(corr)
fig(18, 16)
#Modeling
newPrice <- price[,-c(1,2,3,4,5,7,8,9,11,16,19,20,21)]

head(newPrice)
set.seed(2021)

testID3 <- sample(1:nrow(newPrice), round(nrow(newPrice)*0.7))
priceTrain <- newPrice[-testID3, ]
priceTest <- newPrice[testID3, ]
newPriceModel <- glm(range ~ .,family = binomial(), data=priceTrain)
summary(newPriceModel)
#성능평가_함수
perf_eval <- function(cm){
  # true positive rate
  TPR = Recall = cm[2,2]/sum(cm[2,])
  # precision
  Precision = cm[2,2]/sum(cm[,2])
  # true negative rate
  TNR = cm[1,1]/sum(cm[1,])
  # accuracy
  ACC = sum(diag(cm)) / sum(cm)
  # balance corrected accuracy (geometric mean)
  BCR = sqrt(TPR*TNR)
  # f1 measure
  F1 = 2 * Recall * Precision / (Recall + Precision)
  
  re <- data.frame(TPR = TPR,
                   Precision = Precision,
                   TNR = TNR,
                   ACC = ACC,
                   BCR = BCR,
                   F1 = F1)
  return(re)
}
#성능평가
pred_prob <- predict(newPriceModel, priceTest, type="response")
pred_clas <- rep(0, nrow(priceTest))
pred_clas[pred_prob > 0.5] <- 1
cm <- table(pred=pred_clas, actual=priceTest$range)
perf_eval(cm)

#변수선택법
price <- price[,-c(21)]
testID4 <- sample(1:nrow(price), round(nrow(price)*0.7))
priceTrain <- price[-testID4, ]
priceTest <- price[testID4, ]
priceModel <- glm(range ~ .,family = binomial(), data=priceTrain)
#forward
priceFor <- step(glm(range ~ 1,priceTrain, family = binomial()), direction = "forward", trace = 0, scpoe = formula(priceModel))
pred_prob <- predict(priceFor, priceTest, type="response")
pred_clas <- rep(0, nrow(priceTest))
pred_clas[pred_prob > 0.5] <- 1
cm <- table(pred=pred_clas, actual=priceTest$range)
perf_eval(cm)
summary(priceFor)
#backward
priceBack <- step(glm(range ~ ., priceTest, family = binomial()), direction = "backward", trace = 0, scope = list(lower=range ~ 1, upper=formula(priceModel)))
pred_prob <- predict(priceBack, priceTest, type="response")
pred_clas <- rep(0, nrow(priceTest))
pred_clas[pred_prob > 0.5] <- 1
cm <- table(pred=pred_clas, actual=priceTest$range)
perf_eval(cm)
summary(priceBack)
#stepwise
priceStep <- step(glm(range ~ ., priceTest, family = binomial()), direction = "both", trace = 0, scope = list(lower=range ~ 1, upper=formula(priceModel)))
pred_prob <- predict(priceStep, priceTest, type="response")
pred_clas <- rep(0, nrow(priceTest))
pred_clas[pred_prob > 0.5] <- 1
cm <- table(pred=pred_clas, actual=priceTest$range)
perf_eval(cm)
summary(priceStep)
