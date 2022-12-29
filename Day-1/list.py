nums= [25,23,34,53,43,"mainul","navin","kudus"]
print(nums)
print(nums[-1])

print(nums.append(54),nums)

print(nums.insert(4,'karim'),nums)

print(nums.remove('karim'),nums)

print(nums.pop(4),nums)

print(nums.index('mainul'),nums)

print(nums.count('mainul'),nums)

del nums[-4:-1]
print(nums)

nums.extend([23,43,15,17,19,28,39])
print(nums)

print(nums.sort(),nums)

print(min(nums))

print(max(nums))

print(sum(nums))

