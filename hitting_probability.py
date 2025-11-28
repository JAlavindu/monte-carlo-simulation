def hitting_prob(hitting_count, total_throws):
    if total_throws == 0:
        return 0
    return (hitting_count / total_throws)*100