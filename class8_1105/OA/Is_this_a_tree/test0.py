"""
A binary tree is represented as a sequence of parent-child pairs, for example:
    (A,B) (A,C) (B,G) (C,H) (E,F) (B,D) (C,E)

The following is a recursive definition for the S-expression of a tree:
    S-exp(node) = ( node->val (S-exp(node->first_child))(S-exp(node->second_child))), if node != NULL = "", node == NULL
    where, first_child->val < second_child->val (first_child->val is lexicographically smaller than second_child-> val)

This tree can be represented in an S-expression in multiple ways. The lexicographically smallest way of
expressing it is as follows:
    (A(B(D)(G))(C(E(F))(H)))

Translate the node-pair representation into its lexicographically smallest S-expression or report any errors
that do not conform to the definition of a binary tree.

The list of errors with their codes is as follows:
    Error Code Type of error
    E1      More than 2 children
    E2      Duplicate Edges
    E3      Cycle present (node is direct descendant of more than one node)
    E4      Multiple roots
    E5      Any other error

Function Description
    Complete the function sExpression in the editor below. The function must return either the lexicographically
    lowest S-expression or the lexicographically lowest error code as a string.

    sExpression has the following parameter(s):
    nodes: a string of space-separated parenthetical elements, each of which contains the names of two
    connected nodes separated by a comma

Constraints:
    1. All node names are single characters in the range ascii[A-Z]
    2. The maximum node count is 26.
    3. There is no specific order to the input (parent, child) pairs.

Sample Input 0
    (B,D) (D,E) (A,B) (C,F) (E,G) (A,C)
Sample Output 0
    (A(B(D(E(G))))(C(F)))

Sample Input 1
    (A,B) (A,C) (B,D) (D,C)
Sample Output 1
    E3
Explanation 1
    Node C is a child of nodes A and D. Since D tries to attach itself as parent to a node already above it in the tree,
    this forms a cycle.
"""

#
# Complete the 'sExpression' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING nodes as parameter.
#
def sExpression(nodes):