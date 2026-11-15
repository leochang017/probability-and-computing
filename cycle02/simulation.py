import math
import random
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common.sim import report

# the data file sits in the same folder as this program
DATA_FILE = Path(__file__).resolve().parent / "SMSSpamCollection.txt"
# how many messages the filter gets to learn from, the rest are saved for testing
N_TRAIN = 5000
# fixed seed so the shuffle is the same every run and the numbers don't change
SEED = 0


def load_messages(path):
    # will end up as a list of (label, text) pairs like ("spam", "WINNER!! You have won...")
    messages = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            # each line looks like: label <tab> message, so split on the first tab only
            label, text = line.rstrip("\n").split("\t", 1)
            messages.append((label, text))
    return messages


def get_words(text):
    # make everything lowercase so "FREE" and "free" count as the same word,
    # then pull out every run of letters (this drops punctuation and numbers)
    return re.findall(r"[a-z]+", text.lower())


def train(messages):
    # how many messages of each kind I've seen
    message_counts = {"spam": 0, "ham": 0}
    # for each kind, a dictionary of word -> how many times that word showed up
    word_counts = {"spam": {}, "ham": {}}
    # for each kind, how many words there were in total
    total_words = {"spam": 0, "ham": 0}
    # every different word seen anywhere, a set so nothing is counted twice
    vocabulary = set()

    for label, text in messages:
        message_counts[label] += 1
        for word in get_words(text):
            word_counts[label][word] = word_counts[label].get(word, 0) + 1
            total_words[label] += 1
            vocabulary.add(word)

    return message_counts, word_counts, total_words, vocabulary


def spam_probability(text, model):
    message_counts, word_counts, total_words, vocabulary = model
    n_messages = message_counts["spam"] + message_counts["ham"]

    # scores holds one running score per label
    # probabilities
    scores = {}
    for label in ["spam", "ham"]:
        # start with the prior: what fraction of all messages are this kind, before reading any words
        scores[label] = math.log(message_counts[label] / n_messages)
        for word in get_words(text):
            # skip words the filter never saw in training, it knows nothing about them
            if word not in vocabulary:
                continue
            # P(word | label): how often this word shows up in this kind of message.
            count = word_counts[label].get(word, 0)
            p_word = (count + 1) / (total_words[label] + len(vocabulary))
            # the "naive" part: pretend the words are independent given the label,
            # so their probabilities multiply (which is adding in logs)
            scores[label] += math.log(p_word)

    # Bayes' rule: P(spam | words) = spam score / (spam score + ham score).
    # dividing top and bottom by the spam score gives 1 / (1 + ham/spam), and in logs
    # ham/spam is exp(ham log score - spam log score)
    difference = scores["ham"] - scores["spam"]
    # if ham is ahead by this much the answer is 0 to 16 decimal places, and exp() would overflow
    if difference > 700:
        return 0.0
    return 1 / (1 + math.exp(difference))


def check_bayes_on_one_word(word, train_set):
    # count how many spam and ham messages there are, and how many of each contain the word
    n_spam = n_ham = spam_with_word = ham_with_word = 0
    for label, text in train_set:
        has_word = word in get_words(text)
        if label == "spam":
            n_spam += 1
            if has_word:
                spam_with_word += 1
        else:
            n_ham += 1
            if has_word:
                ham_with_word += 1

    # the direct way: out of all the messages that contain the word, what fraction are spam
    direct = spam_with_word / (spam_with_word + ham_with_word)

    # the Bayes' rule way
    p_spam = n_spam / (n_spam + n_ham)             # P(spam)
    p_word_given_spam = spam_with_word / n_spam    # P(word | spam)
    p_word_given_ham = ham_with_word / n_ham       # P(word | ham)
    # law of total probability for the bottom: P(word) = P(word|spam)P(spam) + P(word|ham)P(ham)
    p_word = p_word_given_spam * p_spam + p_word_given_ham * (1 - p_spam)
    bayes = p_word_given_spam * p_spam / p_word

    print(f"  P(spam) = {p_spam:.4f}, P('{word}' | spam) = {p_word_given_spam:.4f}, P('{word}' | ham) = {p_word_given_ham:.4f}")
    # report prints "simulated" and "exact": here simulated is the direct count and exact is Bayes' rule
    report(f"P(spam | message contains '{word}')", direct, bayes)


def main():
    messages = load_messages(DATA_FILE)
    # shuffle so the training and test messages are a random split
    random.Random(SEED).shuffle(messages)
    # first 5,000 to learn from
    train_set = messages[:N_TRAIN]
    test_set = messages[N_TRAIN:]

    model = train(train_set)
    message_counts = model[0]
    print(f"trained on {len(train_set)} messages ({message_counts['spam']} spam, {message_counts['ham']} ham)")
    print(f"testing on {len(test_set)} messages the filter has never seen")
    print()

    # go through the test messages and keep score
    correct = 0
    spam_total = spam_caught = 0
    ham_total = ham_flagged = 0
    for label, text in test_set:
        # call it spam if the filter thinks spam is more likely than not
        guess = "spam" if spam_probability(text, model) > 0.5 else "ham"
        if guess == label:
            correct += 1
        if label == "spam":
            spam_total += 1
            if guess == "spam":
                spam_caught += 1
        else:
            ham_total += 1
            if guess == "spam":
                ham_flagged += 1

    print(f"accuracy: {correct}/{len(test_set)} = {correct / len(test_set):.4f}")
    print(f"spam caught: {spam_caught}/{spam_total}")
    print(f"real messages wrongly called spam: {ham_flagged}/{ham_total}")
    # the lazy filter that says "ham" every time, to show the accuracy above isn't free
    print(f"always guessing ham would get: {ham_total}/{len(test_set)} = {ham_total / len(test_set):.4f}")
    print()

    # check Bayes' rule by hand on a single word
    check_bayes_on_one_word("free", train_set)
    print()

    # try the filter on messages typed after the file name, or on these two if nothing was typed
    examples = sys.argv[1:]
    if not examples:
        examples = [
            "Congratulations! You have won a free prize, call now to claim",
            "hey are we still on for lunch tomorrow",
        ]
    for text in examples:
        print(f"P(spam) = {spam_probability(text, model):.4f} | {text}")


if __name__ == "__main__":
    main()
