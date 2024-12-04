print('hello, world!')

input = open('day1/data1', 'r')
data = input.read()
lines = data.splitlines()
input.close()

col1 = []
col2 = []

# for line in lines:
#     left_val, right_val = line.split('   ')
#     col1.append(int(left_val))
#     col2.append(int(right_val))
# 
# col1.sort()
# col2.sort()
# 
# sum = 0
# 
# for i in range(len(col1)):
#     sum += abs(col1[i] - col2[i])
# 
# print(sum)

occurrence_score = {}

for line in lines:
    left_val, right_val = line.split('   ')
    occurrence_score[right_val] = occurrence_score.get(right_val, 0) + 1
    col1.append(left_val)

for key in occurrence_score:
    occurrence_score[key] = occurrence_score[key] * int(key)

sim_score = 0

for num_str in col1:
    sim_score += occurrence_score.get(num_str, 0)

print(sim_score)