def min_pts(limit):
   return lambda pts: pts>=limit

thresholds = [70, 40, 30]
scores = [37,51,44,23,78,92,39,84,83,51]
for threshold in thresholds:
   passed = list(filter(min_pts(threshold), scores))
   print(f"Min {threshold} pts: {passed}")

