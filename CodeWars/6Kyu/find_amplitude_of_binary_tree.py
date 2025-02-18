def tree_amplitude(root_node):
    def amplitude(node, cur_min=None, cur_max=None):
        if node is None:
            if cur_min is None:
                return 0
            else:
                return cur_max - cur_min
                
        if cur_min is None:
            cur_min = cur_max = node.data
        else:
            cur_min = min(cur_min, node.data)
            cur_max = max(cur_max, node.data)
            
        return max(amplitude(node.left, cur_min, cur_max),
                  amplitude(node.right, cur_min, cur_max))
                  
    return amplitude(root_node)