import os


# picking each element from set and write to the file
def set_to_file(link_set, file_name):
    delete_file_contents(file_name)
    for link in link_set:
        append_to_file(file_name, link)


# create project directory that contains queue and crawled files
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('CREATING PROJECT ' + directory)
        os.mkdir(directory)


# creating queue and crawled files if not created
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'

    if not os.path.isfile(queue):
        write_file(queue, base_url)

    if not os.path.isfile(crawled):
        write_file(crawled, '')


# writing data to file of given path
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


def delete_file_contents(path):
    with open(path, 'w'):
        pass


# reading each url and add to a set
def file_to_set(file_name):
    result = set()
    with open(file_name, 'rt') as f:
        for line in f:
            result.add(line.replace('\n',''))
    return result








