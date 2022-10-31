import os

folder = "./topimages/"
count = 1

for file_name in os.listdir(folder):
    source = folder + file_name
    updated_name = folder + file_name.replace(" ", "_")
    destination = folder + "sales_" + str(count) + ".txt"
    os.rename(source, updated_name)
    count += 1

print('All Files Renamed')
print('New Names are')
res = os.listdir(folder)
print(res)