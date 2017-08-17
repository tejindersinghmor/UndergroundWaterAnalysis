def create_decision_tree(self, training_samples, predicting_features):
    """Recursively, create a desition tree and return the parent node."""

    if not predicting_features:
        # No more predicting features
        default_klass = self.get_most_common_class(training_samples)
        root_node = DecisionTreeLeaf(default_klass)
    else:
        klasses = [sample.klass for sample in training_samples]
        if len(set(klasses)) == 1:
            target_klass = training_samples[0].klass
            root_node = DecisionTreeLeaf(target_klass)
        else:
            best_feature = self.select_best_feature(training_samples,
                                                    predicting_features,
                                                    klasses)
            # Create the node to return and create the sub-tree.
            root_node = DecisionTreeNode(best_feature)
            best_feature_values = {s.sample[best_feature]
                                   for s in training_samples}
            for value in best_feature_values:
                samples = [s for s in training_samples
                           if s.sample[best_feature] == value]
                # Recursively, create a child node.
                child = self.create_decision_tree(samples,
                                                  predicting_features)
                root_node[value] = child
    return root_node