library(dummies)
library(ggplot2)
library(car)
install.packages("forecast")
install.packages("caret")
library(forecast)
library(caret)

csv1 <- read.csv('../student-mat.csv')
head(csv1)

dim(csv1)
sum(is.na(csv1))
csv1 <- na.omit(csv1)

#--전처리--#
#이진 값(YES:1/NO:0으로 변환)
csv1$schoolsup <- ifelse(csv1$schoolsup == 'yes', 1, 0)
csv1$famsup <- ifelse(csv1$famsup == 'yes', 1, 0)
csv1$paid <- ifelse(csv1$paid == 'yes', 1, 0)
csv1$activities <- ifelse(csv1$activities == 'yes', 1, 0)
csv1$nursery <- ifelse(csv1$nursery == 'yes', 1, 0)
csv1$higher <- ifelse(csv1$higher == 'yes', 1, 0)
csv1$internet <- ifelse(csv1$internet == 'yes', 1, 0)
csv1$romantic <- ifelse(csv1$romantic == 'yes', 1, 0)

#범주형 변수 수치형 변수로 변환
student1 <- dummy.data.frame(csv1)
head(student1)
summary(student1)

#범주형 변수(이진값처럼 변환)
student2 <- data.frame(csv1)
student2$school <- ifelse(student2$school == 'GP', 1, 0) #학교가 GP면 1
student2$sex <- ifelse(student2$sex == 'F', 1, 0) #여성이면 1
student2$address <- ifelse(student2$address == 'U', 1, 0) #도시 거주면 1
student2$famsize <- ifelse(student2$famsize == 'GT3', 1, 0) #가족 수가 3명보다 많으면 1
student2$Pstatus <- ifelse(student2$Pstatus == 'T', 1, 0) #부모가 같이 살면 1
student2$guardian <- ifelse(student2$guardian == 'mother', 1, 0) #보호자가 엄마면 1
head(student2)

#EDA (Bar plot, scatter plot, pie chart, histogram, correlation matrix)
#EDA-age
table(csv1$age)
var(csv1$age)
age <- ggplot(data=csv1,aes(x=age))+
  geom_histogram(binwidth = 0.50, fill='skyblue', color='white')+
  ggtitle("Age of students")
age
#EDA-gender
table(csv1$sex)
gender <- ggplot(data=csv1,aes(x=sex,fill=sex))+
  geom_bar()+
  scale_fill_brewer(palette=2)+
  ggtitle("Sex of students")
gender
#EDA-G3
table(csv1$G3)
grade <- ggplot(data=csv1,aes(x=G3))+
  geom_histogram(binwidth = 0.50, fill='skyblue', color='white')+
  ggtitle("Grade3 of students")
grade

#G1/G2제거
student2 <- student2[,-c(31,32)]
#카테고리변수제거
student2 <- student2[,-c(9,10,11)]

#Modeling_csv1
set.seed(2021)
# testID1 <- sample(1:nrow(csv1),round(nrow(csv1)*0.7))
# csv1Train <- csv1[-testID1,]
# csv1Test <- csv1[testID1,]
# csv1Model <- lm(G3 ~ ., data=csv1)
# summary(csv1Model)
# Modeling_newcsv1
# newtestID1 <- sample(1:nrow(newcsv1),round(nrow(newcsv1)*0.7))
# newcsv1Train <- newcsv1[-newtestID1,]
# newcsv1Test <- newcsv1[newtestID1,]
# newcsv1Model <- lm(G3 ~ ., data=newcsv1)
# summary(newcsv1Model)
# Modeling_student2
testID2 <- sample(1:nrow(student2),round(nrow(student2)*0.7))
student2Train <- student2[-testID2,]
student2Test <- student2[testID2,]
student2Model <- lm(G3 ~ ., data=student2)
summary(student2Model)
student2Model <- lm(G3 ~ age+
                    activities+
                    famrel+
                    absences+
                      G1+G2, data=student2)
#Model Analysis_all
par(mfrow = c(2,2))
plot(student2Model)
#Model Analysis_student2
par(mfrow = c(1,1))
plot(student2Model, which = 1) #Residuals vs Fitted
plot(student2Model, which = 2) #Normal Q-Q
plot(student2Model, which = 3) #Scale-Location
plot(student2Model, which = 4) #Cook's distance
plot(student2Model, which = 5) #Residuals vs Leverage

#성능평가(MSE / MAE 각각 측정)
student2Predict <- predict(student2Model, newdata = student2Test)
mean((student2Test$G3 - student2Predict)**2)
caret::MAE(student2Predict,student2Test$G3)
accuracy(student2Model)

#변수선택법
#forward
student2Forward <- step(student2Model, direction = "forward")
summary(student2Forward)
#backward
student2Backward <- step(student2Model, direction = "backward")
summary(student2Backward)
#Stepwise
student2Stepwise <- step(student2Model, direction = "both")
summary(student2Stepwise)