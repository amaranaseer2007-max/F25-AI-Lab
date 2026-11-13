
import math


def minimax(depth, index, max_turn, scores, target_depth, counter):
    if depth == target_depth:
        counter["leaves"] += 1
        return scores[index]

    if max_turn:
        left = minimax(depth + 1, index * 2, False,
                       scores, target_depth, counter)
        right = minimax(depth + 1, index * 2 + 1, False,
                        scores, target_depth, counter)
        return max(left, right)

    left = minimax(depth + 1, index * 2, True,
                   scores, target_depth, counter)
    right = minimax(depth + 1, index * 2 + 1, True,
                    scores, target_depth, counter)
    return min(left, right)


def alpha_beta(depth, index, max_turn, scores,
               target_depth, alpha, beta, stats):

    if depth == target_depth:
        stats["leaves"] += 1
        return scores[index]

    if max_turn:
        value = float("-inf")

        for i in range(2):
            child = alpha_beta(
                depth + 1, index * 2 + i, False,
                scores, target_depth, alpha, beta, stats
            )

            value = max(value, child)
            alpha = max(alpha, value)

            if alpha >= beta:
                stats["cutoffs"] += 1
                stats["pruned_leaves"] += (
                    (1 - i) * 2 ** (target_depth - depth - 1)
                )
                break

        return value

    else:
        value = float("inf")

        for i in range(2):
            child = alpha_beta(
                depth + 1, index * 2 + i, True,
                scores, target_depth, alpha, beta, stats
            )

            value = min(value, child)
            beta = min(beta, value)

            if alpha >= beta:
                stats["cutoffs"] += 1
                stats["pruned_leaves"] += (
                    (1 - i) * 2 ** (target_depth - depth - 1)
                )
                break

        return value


def run_experiment(title, scores, depth):
    print("\n" + "=" * 45)
    print(title)
    print("Leaf Scores:", scores)

    minimax_count = {"leaves": 0}

    mm_value = minimax(
        0, 0, True, scores, depth, minimax_count
    )

    ab_stats = {
        "leaves": 0,
        "pruned_leaves": 0,
        "cutoffs": 0
    }

    ab_value = alpha_beta(
        0, 0, True, scores, depth,
        float("-inf"), float("inf"), ab_stats
    )

    print("Minimax Value:", mm_value)
    print("Minimax Evaluated Leaves:",
          minimax_count["leaves"])

    print("Alpha-Beta Value:", ab_value)
    print("Alpha-Beta Evaluated Leaves:",
          ab_stats["leaves"])
    print("Pruned Leaves:", ab_stats["pruned_leaves"])
    print("Cutoff Events:", ab_stats["cutoffs"])

    print("Same Root Value:", mm_value == ab_value)


# TASK 1: Manual Minimax tree
original_scores = [3, 5, 2, 9, 0, 7]

depth1 = math.ceil(math.log2(len(original_scores)))

padded_scores = original_scores + (
    [0] * (2 ** depth1 - len(original_scores))
)

print("TASK 1: MINIMAX TREE")
print("Original Scores:", original_scores)
print("Padded Scores:", padded_scores)
print("Tree Depth:", depth1)

run_experiment("TASK 1 MINIMAX", padded_scores, depth1)


# TASK 2: Minimax and Alpha-Beta comparison
task2_scores = [3, 5, 2, 9, 3, 5, 2, 9]

run_experiment("TASK 2: ORIGINAL BRANCH ORDER",
               task2_scores, 3)


# TASK 3: Reorder the two branches of the right MIN node
reordered_scores = (
    task2_scores[:4]
    + task2_scores[6:8]
    + task2_scores[4:6]
)

run_experiment("TASK 3: REORDERED BRANCHES",
               reordered_scores, 3)
