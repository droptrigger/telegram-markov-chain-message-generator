import random
import numpy as np

from aiofile import AIOFile


async def write_words(*args):
    """
        Asynchronously writes text to a file by adding a semicolon after each line.

        Args:
            text (str): The text to be written to the file.
            file (str): The path to the file where the text will be written.
    """
    text, file = args
    async with AIOFile(file, "a", encoding="utf-8") as f:
        text = text.replace("\n", ". ").replace("\n\n", ". ")
        await f.write(text + ",")


async def send_and_gen_sentence(file, min=1, max=13):
    """
        Generates a random phrase based on the text provided in the file.

        :param file: File with dialog messages.
        :param min: Minimum number of words to be generated. The default is 0.
        :param max: The maximum number of words in the generated phrase. The default is 13.

        :return:
            str: The generated phrase.

        Please note that this function may encounter errors when trying to open a file or process text.
        In case of an error, the message "I don't even know what to answer..." will be returned.
    """
    try:
        text = open(file, encoding='utf8').read()
        text = text.replace(",", " ")
        corpus = text.split()

        # Creating word pairs
        def make_pairs(corpus):
            for i in range(len(corpus) - 1):
                yield (corpus[i], corpus[i + 1])

        pairs = make_pairs(corpus)

        word_dict = {}

        # Sorting through all the words in pairs from our list of pairs
        for word_1, word_2 in pairs:
            if word_1 in word_dict.keys():
                word_dict[word_1].append(word_2)
            else:
                word_dict[word_1] = [word_2]

        first_word = np.random.choice(corpus)

        chain = [first_word]

        n_words = random.randint(min - 1, max - 1)
        for i in range(n_words):
            chain.append(np.random.choice(word_dict[chain[-1]]))
        return ' '.join(chain)
    except:
        return "I don't even know what to answer..."