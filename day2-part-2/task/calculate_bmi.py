# bmi stand for body mass index

height = 1.65
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi =  weight / (height ** 2)

print(bmi)

print(int(bmi))
print(round(bmi))

# if we want 2 decimal places we round with 2

print(round(bmi,2))

# assignment opertor

score =0
# user score a point
score += 1
print(score)

# f string used to combine value with the string
height=1.8
is_winning= True
print(f" your score is : {score} ,your height is : {height},your are is : {is_winning}")

print("rc")