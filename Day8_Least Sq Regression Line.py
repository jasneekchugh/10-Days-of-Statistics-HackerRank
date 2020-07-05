#Least Square Regression Line
import statistics as st

n = 5
x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]
mean_x = st.mean(x)
mean_y = st.mean(y)
xy = sum([x[i]*y[i] for i in range(5)])
squared_x = sum([x[i] ** 2 for i in range(5)])


b = ((n * xy) - sum(x) * sum(y)) / (n * squared_x - (sum(x) ** 2))
a = mean_y - b * mean_x

y_pred= a+ 80 *b

print (round(y_pred, 3))
