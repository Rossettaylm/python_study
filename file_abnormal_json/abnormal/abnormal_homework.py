def the_count(filename):
    try:
        cnt = 0
        with open(filename) as file_obj:
            lines = file_obj.readlines()
            for line in lines:
                cnt += line.count('the')
            print("The book has " + str(cnt) + " 'the' word.")
    except FileNotFoundError:
        msg = "The file does not exist!"
        print(msg)

filename = 'dao.txt'
the_count(filename)

def word_count(filename):
    try:
        cnt = 0
        with open(filename) as file_obj:
            contents = file_obj.read()
            cnt = contents.count('me')
        print("The book has " + str(cnt) + " 'the' word.")
    except FileNotFoundError:
        msg = "The file does not exist!"
        print(msg)

filename = 'dao.txt'
word_count(filename)

