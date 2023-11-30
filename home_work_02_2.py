import os

list_of_files = []
for i in range(3):
    file_path = os.path.join(os.getcwd(), f'sorted\\{i + 1}.txt')
    with open(file_path, 'r', encoding='utf-8') as f:
         file_ = f.readlines()
         tuple_ = (len(file_), file_path)
         list_of_files.append(tuple_)

list_of_files = sorted(list_of_files, key=lambda x: x[0])

file_new_path = os.path.join(os.getcwd(), 'total_file.txt')
with open(file_new_path, 'a', encoding='utf-8') as f_new:
    for n, file_path in list_of_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            f_new.write('\n'+str(file_path)[-5:]+'\n')
            f_new.write('\n'+str(n)+'\n')
            for line in f:
                f_new.write(line)

file_new_path = os.path.join(os.getcwd(), 'total_file.txt')
with open(file_new_path, 'r', encoding='utf-8') as f_new:
    print(f_new.read())