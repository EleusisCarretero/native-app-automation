# tmp_str ="{elementId: {id}, percent: {percentage}, velocity: {velocity}}"
# new_str = tmp_str.format(id=40, percentage=0.3, velocity=1.0)
# print(eval(new_str))
example = "{{'{key}': {value}}}"
new_str = example.format(key="10", value=10)
print(eval(new_str))