'''
This program tends to translate a text file which is given as input and translates into a desired language from the use of translate module.
For this, the translate module needs to be installed which can be done via pip, "pip install translate".

The documentation can be read at pypi.org
'''


from translate import Translator

translator = Translator(to_lang="ja")
try:
    with open('./test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('./test-ja.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print("Check your file path")
