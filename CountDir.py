import os
path = "/u/users/kumaran"
num_dir = len([d for d in os.listdir(path)
                if os.path.isdir(os.path.join(path, d))])
print(num_dir)