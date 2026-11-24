
"""
Cricket Score Calculator
Usage:
python cricket_score.py <runs> <overs> <batsman_runs>
                         <balls> <target> <overs_left>
"""

import sys


# Convert cricket overs into total balls
def overs_to_balls(overs):
    whole = int(overs)
    balls = round((overs - whole) * 10)
    return whole * 6 + balls


# Calculate team run rate
def run_rate(runs, overs):
    balls = overs_to_balls(overs)

    if balls <= 0:
        return 0.0

    return round(runs * 6 / balls, 2)


# Calculate batsman's strike rate
def strike_rate(runs, balls):
    if balls <= 0:
        return 0.0

    return round(runs * 100 / balls, 2)


# Calculate required run rate
def required_run_rate(target, current_runs, overs_left):
    runs_needed = target - current_runs

    if runs_needed <= 0:
        return 0.0

    balls_left = overs_to_balls(overs_left)

    if balls_left <= 0:
        return float("inf")

    return round(runs_needed * 6 / balls_left, 2)


# Display match status
def match_status(target, current_runs):
    if current_runs >= target:
        return "Target Achieved"

    return f"Need {target - current_runs} more runs to win"


# Main function
def main():
    if len(sys.argv) != 7:
        print("Usage: python cricket_score.py "
              "<runs> <overs> <batsman_runs> "
              "<balls> <target> <overs_left>")
        return

    runs = int(sys.argv[1])
    overs = float(sys.argv[2])
    batsman_runs = int(sys.argv[3])
    balls = int(sys.argv[4])
    target = int(sys.argv[5])
    overs_left = float(sys.argv[6])

    print("===== Cricket Score Calculator =====")
    print(f"Team score       : {runs} runs in {overs} overs")
    print(f"Run rate         : {run_rate(runs, overs)}")
    print(f"Batsman          : {batsman_runs} off {balls} balls")
    print(f"Strike rate      : {strike_rate(batsman_runs, balls)}")
    print(f"Target           : {target} ({overs_left} overs left)")
    print(f"Required run rate: {required_run_rate(target, runs, overs_left)}")
    print(f"Match status     : {match_status(target, runs)}")


if __name__ == "__main__":
    main()
