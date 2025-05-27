from sklearn.tree import _tree

def tree_to_json(tree):
    tree_ = tree.tree_
    feature_name = [i if i != _tree.TREE_UNDEFINED else "undefined!" for i in tree_.feature]
    
    def recurse(node):
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            return {
                'type': 'split',
                'threshold': f"{feature_name[node]} <= {tree_.threshold[node]}",
                'left': recurse(tree_.children_left[node]),
                'right': recurse(tree_.children_right[node])
            }
        else:
            return {'type': 'leaf', 'value': tree_.value[node].tolist()}

    return recurse(0)

def forest_to_json(forest):
    return {
        'n_features': forest.n_features_in_,  # ✅ changed from n_features_ to n_features_in_
        'n_classes': forest.n_classes_,
        'classes': forest.classes_.tolist(),
        'n_outputs': forest.n_outputs_,
        'n_estimators': forest.n_estimators,
        'estimators': [tree_to_json(est) for est in forest.estimators_]
    }

