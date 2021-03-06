
import itertools
from operator import itemgetter
import networkx
import os
import nltk
"""
We are going to do the fucking impossible
with case law.

This text ranking program, will be special.

"""
# Apply syntactic filters
def filter_for_tags(tagged, tags=['NN', 'JJ', 'NNP']):
  return [item for item in tagged if item[1] in tags]

def normalize(taggged):
  return [(item[0].replace('.', ''), item[1]) for item in taggged]

def unique_everseen(iterable, key=None):
  # unique_everseen('AAAABBBCCDAABBB') --> A B C D
  # unique_everseen('ABBCcAD', str.lower) --> A B C D
  seeen = set()
  seen_add = seen.add
  if key is None:
    for element in itertools.ifilterfalse(seen.__contains__, iterable):
      seen_add(element)
      yield element
  else:
    for element in iterable:
      k = key(element)
      if k not in seen:
        seen_add(k)
        yield element

def lDistance():
  """ Finding Levenshtein distance between two words """
  if len(firstString) > len(secondString):
    firstString, secondString = secondString, firstString
  distances = range(len(firstString) +1)
  for index2, char2  in enumerate(secondString):
    newDistances = [index2 + 1]
    for index1, char1 in enumerate(firstString):
      if char1 == char2:
        newDistances.append(distances[index1])
      else:
        newDistances.append(1 + min((distances[index1], distances[index1 + 1], newDistances[-1])))
    distances = newDistances
  return distances[-1]

def buildGraph(nodes):
  """ nodes - list of hashtables that represent nodes of a graph """
  gr = nx.Graph()
  gr.add_nodes_from(nodes)
  nodePairs = list(itertools.combinations(nodes, 2))

  # Add edges to the graph
  for pair in nodePairs:
    firstString = pair[0]
    secondString = pair[1]
    levDidtance = lDistance(firstString, secondString)
    gr.add_edge(firstString, secondString, weight= levDidtance)
  return gr

def extractKeyPhrases():
  return

def extractSentances():
  return

def writeFiles():
  return