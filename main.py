from hits_or_miss import hit_miss
from hitting_probability import hitting_prob
from write_to_excel import excel_writer
import random
import statistics

def main():
    while True:
        try:
            # Number of dart throws
            N = int(input("Enter the number of dart throws: "))
            if N > 0:
                break
            else:
                print("Please enter a positive integer for the number of throws.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    
    milestones = [1000, 10000, 100000, 1000000]
    # Only consider milestones up to N
    active_milestones = [m for m in milestones if m <= N]
    
    # If N is not in milestones, you might want to include it, 
    # but based on previous context, we stick to the milestones.
    # If N < 1000, active_milestones is empty. Let's handle that if needed, 
    # but assuming user inputs large N as per context.
    
    all_data = []

    print(f"Running simulation 10 times for {N} throws...")

    for experiment_id in range(1, 11):
        # print(f"  Experiment {experiment_id}/10...")
        total_hitting_count = 0
        
        # We simulate up to the largest milestone needed
        # If active_milestones is empty (N < 1000), we might skip or just run N.
        # Let's assume we just run up to N if no milestones, or just the milestones.
        # The prompt implies we want to check convergence at milestones.
        
        targets = sorted(active_milestones)
        if not targets and N > 0:
             targets = [N] # Fallback if N < 1000
        
        current_throw_count = 0
        previous_target = 0
        
        for target in targets:
            throws_needed = target - previous_target
            
            # Throw darts
            for _ in range(throws_needed):
                x = random.uniform(-1, 1)
                y = random.uniform(-1, 1)
                h, m = hit_miss(x, y)
                total_hitting_count += h
            
            current_throw_count = target
            previous_target = target
            
            # Record data for this milestone
            all_data.append({
                'Experiment ID': experiment_id,
                'Total Throws': current_throw_count,
                'Total Hitting Count': total_hitting_count
            })

    # Process data for Excel
    final_records = []
    
    # Get unique throw counts we processed
    unique_throws = sorted(list(set(d['Total Throws'] for d in all_data)))
    
    for throw_count in unique_throws:
        # Filter data for this throw count
        subset = [d for d in all_data if d['Total Throws'] == throw_count]
        
        hits_list = [d['Total Hitting Count'] for d in subset]
        pi_list = []
        
        # Add individual experiment rows
        for d in subset:
            pi_val = (d['Total Hitting Count'] / d['Total Throws']) * 4
            pi_list.append(pi_val)
            
            final_records.append({
                'Experiment ID': d['Experiment ID'],
                'total throws': d['Total Throws'],
                'total hitting count': d['Total Hitting Count'],
                'hitting probability (%)': round((d['Total Hitting Count'] / d['Total Throws']) * 100, 2),
                'estimated value of Pi': round(pi_val, 6)
            })
            
        # Calculate Mean
        mean_pi = statistics.mean(pi_list)
        mean_hits = statistics.mean(hits_list)
        
        final_records.append({
            'Experiment ID': 'Mean',
            'total throws': throw_count,
            'total hitting count': mean_hits,
            'hitting probability (%)': round((mean_hits / throw_count) * 100, 2),
            'estimated value of Pi': round(mean_pi, 6)
        })
        
        # Calculate Mode
        try:
            mode_pi = statistics.mode(pi_list)
        except statistics.StatisticsError:
            mode_pi = "N/A" # No unique mode
            
        try:
            mode_hits = statistics.mode(hits_list)
        except statistics.StatisticsError:
            mode_hits = "N/A"

        final_records.append({
            'Experiment ID': 'Mode',
            'total throws': throw_count,
            'total hitting count': mode_hits,
            'hitting probability (%)': "N/A" if mode_hits == "N/A" else round((mode_hits / throw_count) * 100, 2),
            'estimated value of Pi': mode_pi if mode_pi == "N/A" else round(mode_pi, 6)
        })

    # Write to Excel
    if final_records:
        excel_writer(final_records)
        
    # Print summary for the last run (or mean of last run) to terminal
    # The user expects some output. Let's print the Mean for the largest N.
    if unique_throws:
        max_throws = unique_throws[-1]
        mean_rec = next(r for r in final_records if r['Experiment ID'] == 'Mean' and r['total throws'] == max_throws)
        print(f"\nSummary for {max_throws} throws (Mean of 10 experiments):")
        print(f"Mean hitting count: {mean_rec['total hitting count']}")
        print(f"Mean Hitting Probability: {mean_rec['hitting probability (%)']} %")
        print(f"Mean Estimated Pi: {mean_rec['estimated value of Pi']}")
        

if __name__ == "__main__":
    main() 