class LCA(object):

	
	def lowestCommonAncestor(self, root, p, q):
		if root in (None, p, q):
			return root
		left, right = [self.lowestCommonAncestor(child, p, q) \
		for child in (root.left, root.right)]
		# 1. If the current subtree contains both p and q,
		#    return their LCA.
		# 2. If only one of them is in that subtree,
		#    return that one of them.
		# 3. If neither of them is in that subtree,
		#    return the node of that subtree.
		return root if left and right else left or right


	def LCA4DAG(self, graph, a, b):
		#check that the graph is of the correct type
		assert nx.is_directed_acyclic_graph(graph)
		return 0