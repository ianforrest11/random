
import json

def install_sort(package):
    return package['analytics']['30d']

with open('package_info.json', 'r') as f:
    data = json.load(f)

# no parenthesis, not executing function, just passing it in
data.sort(key=install_sort, reverse=True)

# dump json to string with dumps
# print top 5 most downloaded homebrew packages
data_str = json.dumps(data[:5], indent=2)
print(data_str)