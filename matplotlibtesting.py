import matplotlib.pyplot as plt, pandas as pd, numpy as np

# plt.figure(figsize=(8,4))
# x = [1,2,3,4,5]
# y = [2,4,6,8,10]


# plt.plot(x,y)
# plt.title("Practice Plot")
# plt.xlabel("X values")
# plt.ylabel("Y values")
# # plt.show()

# plt.figure(figsize=(8, 4))
# win_percentages = [0.6, 0.55, 0.7, 0.48, 0.62, 0.59, 0.66, 0.52, 0.58, 0.61]
# plt.hist(win_percentages, bins=5, color='green', alpha=0.5)  
# plt.title("Distribution of Win Percentages")
# plt.xlabel("Win Percentage")
# plt.ylabel("Number of Teams")
# plt.show()








# plt.figure(figsize=(12, 10))
# win_percentages = [0.6, 0.55, 0.7, 0.48, 0.62, 0.59, 0.66, 0.52, 0.58, 0.61]
# # Original histogram
# plt.subplot(2, 2, 1)
# plt.hist(win_percentages, bins=5, color='green', alpha=0.7, edgecolor="black")
# plt.title("Original: bins=5, green, alpha=0.7")
# plt.xlabel("Win Percentage")
# plt.ylabel("Number of Teams")

# # Show what different bin numbers do
# plt.subplot(2, 2, 2)
# plt.hist(win_percentages, bins=3, color='red', alpha=0.7, edgecolor="black")
# plt.title("Different bins: bins=3")
# plt.xlabel("Win Percentage")
# plt.ylabel("Number of Teams")

# # Show what different alpha does
# plt.subplot(2, 2, 3)
# plt.hist(win_percentages, bins=5, color='blue', alpha=0.3, edgecolor="black")
# plt.title("More transparent: alpha=0.3")
# plt.xlabel("Win Percentage")
# plt.ylabel("Number of Teams")

# # Show with more bins
# plt.subplot(2, 2, 4)
# counts, bin_edges, patches = plt.hist(win_percentages, bins=10, color='purple', alpha=0.8, edgecolor="black")
# plt.xticks(bin_edges)
# plt.title("More bins: bins=10")
# plt.xlabel("Win Percentage")
# plt.ylabel("Number of Teams")


# plt.tight_layout()
# plt.show()



# ####test 2
# Create sample hockey data to work with
sample_data = {
    'Team Name': ['Rangers', 'Bruins', 'Leafs', 'Flyers', 'Kings', 'Hawks', 'Wings', 'Sharks'],
    'Goals For': [220, 240, 210, 190, 180, 200, 195, 225],
    'Goals Against': [200, 180, 190, 220, 210, 195, 205, 185],
    'Win %': [0.65, 0.72, 0.58, 0.45, 0.42, 0.55, 0.48, 0.68]
}
df = pd.DataFrame(sample_data)







# # ===============================================
# # PART 2: COLOR MAPS (CMAPS) EXPLAINED
# # ===============================================

# print("=== PART 2: DIFFERENT COLOR MAPS ===")

# # Show different color maps
# fig, axes = plt.subplots(2, 3, figsize=(15, 8))
# cmaps = ['RdYlGn', 'viridis', 'coolwarm', 'plasma', 'Blues', 'Reds']

# for i, cmap in enumerate(cmaps):
#     row = i // 3
#     col = i % 3
    
#     scatter = axes[row, col].scatter(df['Goals For'], df['Goals Against'], 
#                                    c=df['Win %'], cmap=cmap, s=100)
#     axes[row, col].set_title(f"Colormap: {cmap}")
#     axes[row, col].set_xlabel("Goals For")
#     axes[row, col].set_ylabel("Goals Against")
#     plt.colorbar(scatter, ax=axes[row, col])

# plt.tight_layout()
# plt.show()

# print("Popular colormaps:")
# print("- 'RdYlGn': Red-Yellow-Green (good for performance data)")
# print("- 'viridis': Purple to Yellow (colorblind friendly)")
# print("- 'coolwarm': Blue-White-Red (good for +/- data)")
# print("- 'plasma': Purple to Pink to Yellow")
# print("- 'Blues': Light to Dark Blue")
# print()


# # ===============================================
# # PART 3: SCATTER PLOT PARAMETERS EXPLAINED
# # ===============================================

# print("=== PART 3: SCATTER PLOT PARAMETERS ===")

# plt.figure(figsize=(15, 5))

# # Parameter: s (size)
# plt.subplot(1, 3, 1)
# plt.scatter(df['Goals For'], df['Goals Against'], 
#            c=df['Win %'], cmap='RdYlGn', 
#            s=df['Win %']*500)  # Size proportional to Win %
# plt.title("Size = Win % * 500")
# plt.xlabel("Goals For")
# plt.ylabel("Goals Against")

# # Parameter: alpha (transparency)
# plt.subplot(1, 3, 2)
# plt.scatter(df['Goals For'], df['Goals Against'], 
#            c=df['Win %'], cmap='RdYlGn', 
#            s=150, alpha=0.3)  # Very transparent
# plt.title("Alpha = 0.3 (transparent)")
# plt.xlabel("Goals For")
# plt.ylabel("Goals Against")

# # Parameter: edgecolors (outline)
# plt.subplot(1, 3, 3)
# plt.scatter(df['Goals For'], df['Goals Against'], 
#            c=df['Win %'], cmap='RdYlGn', 
#            s=150, alpha=0.8, edgecolors='black', linewidth=2)
# plt.title("With Black Edges")
# plt.xlabel("Goals For")
# plt.ylabel("Goals Against")

# plt.tight_layout()
# plt.show()

# print("Parameters explained:")
# print("s=100     → Size of dots (can be number or array)")
# print("alpha=0.7 → Transparency (0=invisible, 1=solid)")
# print("edgecolors → Color of dot borders")
# print("linewidth → Thickness of dot borders")
# print()

# # ===============================================
# # PART 4: ANNOTATIONS STEP BY STEP
# # ===============================================

# print("=== PART 4: ANNOTATIONS EXPLAINED ===")

# # Step 1: Basic scatter plot
# plt.figure(figsize=(12, 8))

# plt.subplot(2, 2, 1)
# plt.scatter(df['Goals For'], df['Goals Against'], c=df['Win %'], cmap='RdYlGn', s=100)
# plt.title("Step 1: Basic Plot")
# plt.xlabel("Goals For")
# plt.ylabel("Goals Against")

# # Step 2: Add one annotation manually
# plt.subplot(2, 2, 2)
# plt.scatter(df['Goals For'], df['Goals Against'], c=df['Win %'], cmap='RdYlGn', s=100)
# plt.annotate('Bruins',  # Text to show
#              (240, 180),  # Position of the point (Goals For, Goals Against)
#              xytext=(250, 190),  # Where to put the text
#              arrowprops=dict(arrowstyle='->', color='black'))  # Arrow pointing to dot
# plt.title("Step 2: One Manual Annotation")
# plt.xlabel("Goals For")
# plt.ylabel("Goals Against")

# # Step 3: Add annotations with a loop (all teams)
# plt.subplot(2, 2, 3)
# plt.scatter(df['Goals For'], df['Goals Against'], c=df['Win %'], cmap='RdYlGn', s=100)
# for i, team in enumerate(df['Team Name']):
#     plt.annotate(team, 
#                 (df['Goals For'].iloc[i], df['Goals Against'].iloc[i]),
#                 xytext=(5, 5),  # Offset from the point
#                 textcoords='offset points')  # Use offset instead of absolute position
# plt.title("Step 3: All Teams Labeled (Messy!)")
# plt.xlabel("Goals For")
# plt.ylabel("Goals Against")

# # Step 4: Selective labeling (every 3rd team)
# plt.subplot(2, 2, 4)
# scatter = plt.scatter(df['Goals For'], df['Goals Against'], c=df['Win %'], cmap='RdYlGn', s=100)
# for i, team in enumerate(df['Team Name']):
#     if i % 3 == 0:  # Only every 3rd team (0, 3, 6, ...)
#         plt.annotate(team, 
#                     (df['Goals For'].iloc[i], df['Goals Against'].iloc[i]),
#                     xytext=(5, 5), 
#                     textcoords='offset points',
#                     fontsize=8)
# plt.colorbar(scatter, label='Win %')
# plt.title("Step 4: Every 3rd Team (Clean!)")
# plt.xlabel("Goals For")
# plt.ylabel("Goals Against")

# plt.tight_layout()
# plt.show()

# # ===============================================
# # PART 5: ADVANCED ANNOTATION TECHNIQUES
# # ===============================================

# print("=== PART 5: ADVANCED ANNOTATIONS ===")

# plt.figure(figsize=(15, 5))

# # Technique 1: Label only extreme values
# plt.subplot(1, 3, 1)
# scatter = plt.scatter(df['Goals For'], df['Goals Against'], c=df['Win %'], cmap='RdYlGn', s=100)
# plt.colorbar(scatter, label='Win %')

# # Find teams with highest and lowest Win %
# max_win_idx = df['Win %'].idxmax()  # Index of highest win %
# min_win_idx = df['Win %'].idxmin()  # Index of lowest win %

# # Label only these extreme teams
# for idx in [max_win_idx, min_win_idx]:
#     plt.annotate(f"{df['Team Name'].iloc[idx]}\n({df['Win %'].iloc[idx]:.1%})",
#                 (df['Goals For'].iloc[idx], df['Goals Against'].iloc[idx]),
#                 xytext=(10, 10), textcoords='offset points',
#                 bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
#                 arrowprops=dict(arrowstyle='->', color='black'))

# plt.title("Label Extreme Values Only")
# plt.xlabel("Goals For")
# plt.ylabel("Goals Against")

# # Technique 2: Conditional labeling based on data
# plt.subplot(1, 3, 2)
# scatter = plt.scatter(df['Goals For'], df['Goals Against'], c=df['Win %'], cmap='RdYlGn', s=100)
# plt.colorbar(scatter, label='Win %')

# # Label teams with Win % > 60%
# good_teams = df[df['Win %'] > 0.60]
# for i, row in good_teams.iterrows():
#     plt.annotate(row['Team Name'],
#                 (row['Goals For'], row['Goals Against']),
#                 xytext=(5, 5), textcoords='offset points',
#                 fontsize=8, fontweight='bold', color='darkgreen')

# plt.title("Label High-Performing Teams Only")
# plt.xlabel("Goals For")
# plt.ylabel("Goals Against")

# # Technique 3: Different annotation styles
# plt.subplot(1, 3, 3)
# scatter = plt.scatter(df['Goals For'], df['Goals Against'], c=df['Win %'], cmap='RdYlGn', s=100)
# plt.colorbar(scatter, label='Win %')

# # Different styles for different performance levels
# for i, row in df.iterrows():
#     if row['Win %'] > 0.65:  # Great teams - green box
#         plt.annotate(row['Team Name'],
#                     (row['Goals For'], row['Goals Against']),
#                     xytext=(5, 5), textcoords='offset points',
#                     bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7),
#                     fontsize=8, fontweight='bold')
#     elif row['Win %'] < 0.50:  # Poor teams - red box
#         plt.annotate(row['Team Name'],
#                     (row['Goals For'], row['Goals Against']),
#                     xytext=(5, 5), textcoords='offset points',
#                     bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7),
#                     fontsize=8)

# plt.title("Styled Annotations by Performance")
# plt.xlabel("Goals For")
# plt.ylabel("Goals Against")

# plt.tight_layout()
# plt.show()

# # ===============================================
# # PART 6: PUTTING IT ALL TOGETHER
# # ===============================================

# print("=== PART 6: COMPLETE EXAMPLE ===")

# plt.figure(figsize=(12, 8))

# # Create the main scatter plot
# scatter = plt.scatter(df['Goals For'], df['Goals Against'], 
#                      c=df['Win %'],        # Color by Win %
#                      cmap='RdYlGn',        # Green=good, Red=bad
#                      s=df['Win %']*300,    # Size by Win % too
#                      alpha=0.7,            # Slight transparency
#                      edgecolors='black',   # Black borders
#                      linewidth=1)          # Border thickness

# # Add colorbar
# cbar = plt.colorbar(scatter, label='Win Percentage')
# cbar.ax.tick_params(labelsize=10)

# # Add labels and title
# plt.xlabel("Goals For (Offensive Performance)", fontsize=12)
# plt.ylabel("Goals Against (Defensive Performance)", fontsize=12)
# plt.title("NHL Team Performance: Offense vs Defense\n(Color and Size = Win %)", fontsize=14, fontweight='bold')

# # Add annotations for interesting teams
# # Best team (highest win %)
# best_team_idx = df['Win %'].idxmax()
# plt.annotate(f"Best: {df['Team Name'].iloc[best_team_idx]}\n{df['Win %'].iloc[best_team_idx]:.1%} win rate",
#             (df['Goals For'].iloc[best_team_idx], df['Goals Against'].iloc[best_team_idx]),
#             xytext=(20, 20), textcoords='offset points',
#             bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.8),
#             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2', color='darkgreen'),
#             fontsize=10, fontweight='bold')

# # Worst team (lowest win %)
# worst_team_idx = df['Win %'].idxmin()
# plt.annotate(f"Worst: {df['Team Name'].iloc[worst_team_idx]}\n{df['Win %'].iloc[worst_team_idx]:.1%} win rate",
#             (df['Goals For'].iloc[worst_team_idx], df['Goals Against'].iloc[worst_team_idx]),
#             xytext=(-80, -30), textcoords='offset points',
#             bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral', alpha=0.8),
#             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-0.2', color='darkred'),
#             fontsize=10)

# # Add reference line (where Goals For = Goals Against)
# min_goals = min(df['Goals For'].min(), df['Goals Against'].min())
# max_goals = max(df['Goals For'].max(), df['Goals Against'].max())
# plt.plot([min_goals, max_goals], [min_goals, max_goals], 
#          'k--', alpha=0.5, linewidth=1, label='Equal Goals For/Against')

# # Add grid and legend
# plt.grid(True, alpha=0.3)
# plt.legend(loc='upper left')

# # Add text explanation
# plt.text(0.02, 0.98, "Upper Left = Good Defense, Low Offense\nLower Right = Poor Defense, High Offense", 
#          transform=plt.gca().transAxes, fontsize=9, verticalalignment='top',
#          bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# plt.tight_layout()
# plt.show()

# print("\n=== KEY TAKEAWAYS ===")
# print("1. c=df['column'] colors points based on data values")
# print("2. cmap='RdYlGn' sets the color scheme")
# print("3. plt.colorbar() shows what colors mean")
# print("4. plt.annotate(text, (x,y)) adds labels to specific points")
# print("5. xytext=(5,5) + textcoords='offset points' positions text relative to points")
# print("6. Use loops with conditions to selectively label points")
# print("7. bbox=dict() adds colored backgrounds to annotations")
# print("8. arrowprops=dict() adds arrows pointing to data points")




plt.figure(figsize=(10, 6))
years = [2018, 2019, 2020, 2021, 2022]
team1_wins = [45, 48, 42, 50, 46]
team2_wins = [38, 41, 45, 39, 43]

plt.plot(years, team1_wins, color='blue', marker='o', linewidth=2, label='Team 1')
plt.plot(years, team2_wins, color='red', marker='s', linewidth=2, linestyle='--', label='Team 2')

# plt.show()
x=np.random.randn(1000)
y=np.random.randn(1000)
plt.hist2d(x,y,bins=100,cmap='Blues')
plt.colorbar(label='Density')

plt.figure(figsize=(10,6))
count, bins, patches = plt.hist(x, bins=100)
cmap = plt.cm.get_cmap('coolwarm')
norm = plt.Normalize(count.min(), count.max())

for i, patch in enumerate(patches):
    patch.set_facecolor(cmap(norm(count[i])))
plt.show()