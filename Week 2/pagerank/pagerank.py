import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    name_pages = list(corpus.keys())
    random_proba = (1 - damping_factor) / len(name_pages)
    new_dict = {}
    for i in range(len(name_pages)):
        new_dict[name_pages[i]] = random_proba

    # Get the probabilities from the current page 
    linked_pages = list(corpus[page])
    number_linked_pages = len(linked_pages)
    proba_linked = damping_factor / number_linked_pages

    for name in linked_pages:
        new_dict[name] = new_dict[name] + proba_linked

    return new_dict


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    import numpy as np
    # First sampple. Choosing from a page at random
    name_pages = list(corpus.keys())
    page = random.choice(name_pages)

    # Create the dictionary for the return
    pages_dict = {}
    for i in range(len(name_pages)):
        pages_dict[name_pages[i]] = 0

    # For each sample, the next should be generated based on the previous sample's transition model
    for i in range(n):
        transition_probabilities = transition_model(corpus, page, damping_factor)
        probs = np.array(list(transition_probabilities.values()))
        keys = transition_probabilities.keys()
        page = np.random.choice(keys, size=1, replace=True, p=probs)
        pages_dict[page] += 1

    for i in range(len(name_pages)):
        pages_dict[name_pages[i]] = pages_dict[name_pages[i]]/n

    return pages_dict


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
