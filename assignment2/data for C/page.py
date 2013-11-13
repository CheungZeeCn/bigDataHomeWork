#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# by zhangzhi @2013-11-13 06:54:14 
# Copyright 2013 NONE rights reserved.
# Copy many from networkX's source code
import networkx as nx
from networkx.exception import NetworkXError

def pagerank(G, alpha=0.85, personalization=None,
             max_iter=100, tol=1.0e-8, nstart=None, weight='weight'):
    """Return the PageRank of the nodes in the graph.

    PageRank computes a ranking of the nodes in the graph G based on
    the structure of the incoming links. It was originally designed as
    an algorithm to rank web pages.

    Parameters
    -----------
    G : graph
      A NetworkX graph

    alpha : float, optional
      Damping parameter for PageRank, default=0.85

    personalization: dict, optional
       The "personalization vector" consisting of a dictionary with a
       key for every graph node and nonzero personalization value for each node.

    max_iter : integer, optional
      Maximum number of iterations in power method eigenvalue solver.

    tol : float, optional
      Error tolerance used to check convergence in power method solver.

    nstart : dictionary, optional
      Starting value of PageRank iteration for each node.

    weight : key, optional
      Edge data key to use as weight.  If None weights are set to 1.

    Returns
    -------
    pagerank : dictionary
       Dictionary of nodes with PageRank as value

    Examples
    --------
    >>> G=nx.DiGraph(nx.path_graph(4))
    >>> pr=nx.pagerank(G,alpha=0.9)

    Notes
    -----
    The eigenvector calculation is done by the power iteration method
    and has no guarantee of convergence.  The iteration will stop
    after max_iter iterations or an error tolerance of
    number_of_nodes(G)*tol has been reached.

    The PageRank algorithm was designed for directed graphs but this
    algorithm does not check if the input graph is directed and will
    execute on undirected graphs by converting each oriented edge in the
    directed graph to two edges.

    """
    if type(G) == nx.MultiGraph or type(G) == nx.MultiDiGraph:
        raise Exception("pagerank() not defined for graphs with multiedges.")

    if len(G) == 0:
        return {}

    if not G.is_directed():
        D = G.to_directed()
    else:
        D = G

    # create a copy in (right) stochastic form
    # each row of W sum up to be one
    W = nx.stochastic_graph(D, weight=weight)
    scale = 1.0 / W.number_of_nodes()

    # choose fixed starting vector if not given
    if nstart is None:
        x = dict.fromkeys(W, scale)
    else:
        x = nstart
        # normalize starting vector to 1
        s = 1.0 / sum(x.values())
        for k in x: x[k] *= s

    # assign uniform personalization/teleportation vector if not given
    if personalization is None:
        # teleport
        p = dict.fromkeys(W, scale)
    else:
        # teleport with bias
        p = personalization
        # normalize starting vector to 1
        s = 1.0 / sum(p.values())
        for k in p:
            p[k] *= s
        if set(p) != set(G):
            raise NetworkXError('Personalization vector '
                                'must have a value for every node')


    # "dangling" nodes, no links out from them
    out_degree = W.out_degree()
    dangle = [ n for n in W if out_degree[n]==0.0 ]
    i = 0
    # real 'tol' 
    tol = W.number_of_nodes() * tol
    #
    while True: # power iteration: make up to max_iter iterations
        xlast = x # x is the vector containing the value of page rank
        x = dict.fromkeys(xlast.keys(), 0)
        # dangle nodes have no out links, so we sum all the rank for these 
        # nodes, and then scale it and alpha it for the next step
        # just like making each dangle have pseudo edge to every link to the web
        danglesum = alpha * scale * sum(xlast[n] for n in dangle)
        for n in x:
            # this matrix multiply looks odd because it is
            # doing a left multiply x^T=xlast^T*W  # W is inlink form
            for nbr in W[n]:# linear combination of lines
                x[nbr] += alpha * xlast[n] * W[n][nbr][weight] 
            x[n] += danglesum + (1.0-alpha)*p[n]
        # normalize vector
        s = 1.0 / sum(x.values())
        for n in x:
            x[n] *= s
        # check convergence, l1 norm
        err = sum([abs(x[n]-xlast[n]) for n in x])
        if err < tol: # ok
            break
        if i > max_iter:
            raise NetworkXError('pagerank: power iteration failed to converge '
                                'in %d iterations.'%(i-1))
        i+=1
    return x

if __name__ == '__main__':
    print 'hello world'

