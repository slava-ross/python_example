#!/usr/bin/python3
################################################################################
#
# Task 1
# Read integer numbers sequence from file.
# Find: 90 Percentile, Median (50 Percentile), Maximum, Minimum and Average Values.
# Each number in the file is on a new line.
#
################################################################################

# Processing Array { @data_array }
data_array=[]

# Number Counter { @cnt }
cnt = 0

# Sum of Numbers { @sum }
sum = 0

# Array filling
filename = input( 'Enter Data File name: ' )
with open( filename ) as datafile:
  for line in datafile:
    value = int( line.strip() )
    data_array.append( value )
    sum += value
    cnt += 1

# Array sorting
data_array.sort()

# Finding Percentile
# Percentile index { @idx }
# 90 Percentile { @percent90 }
idx = int( cnt * 0.9 )
percent90 = data_array[idx]
print( '90 percentile', percent90 )

# Finding Median
# Median { @med }
if cnt % 2 == 0:
  med = ( data_array[cnt // 2 - 1] + data_array[cnt // 2] ) / 2
else:
  med = data_array[ cnt // 2 + 1 ]
print( 'median', med )

# Finding Average
# Average { @avg }
avg = sum / cnt
print( 'average', '%.3f' % avg )

# Finding Maximum Value
# Maximum { @max }
max = data_array[-1]
print( 'max', max )

# Finding Minimum Value
# Minimum { @min }
min = data_array[0]
print( 'min', min )
