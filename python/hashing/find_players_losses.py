

def find_players_wins_losses( matches: List[List[int]]) -> List[List[int]]:
        zero_losses = set()
        one_losses = set()
        more_losses = set()
        ans = []
        for winner, loser in matches:
            if winner not in one_losses and winner not in more_losses:
                zero_losses.add(winner)

            if loser in zero_losses:
                zero_losses.remove(loser)
                one_losses.add(loser)
            elif loser in one_losses:
                more_losses.add(loser)
                one_losses.remove(loser)
            elif loser in more_losses:
                continue
            else:
                one_losses.add(loser)

        return [sorted(list(zero_losses)), sorted(list(one_losses))]