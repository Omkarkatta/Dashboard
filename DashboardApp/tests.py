from django.test import TestCase

# Create your tests here.


obj = ["Now, you don't have to mention version number. Visit Homepage for more API endpoints",
        {'active_cases': 283407, 'active_rate': 34.52, 'confirmed_cases': 820915, 'death_cases': 22123,
         'death_rate': 2.69, 'delta_change_active_cases': 6722, 'delta_change_death_cases': 519,
         'delta_change_recovered_cases': 19873, 'last_total_active_cases': 276685, 'last_total_death_cases': 21604,
         'last_total_recovered_cases': 495512, 'last_updated': '11 July 2020, 08:00 IST (GMT+5:30)',
         'migrated_cases': 1, 'passengers_screened': 1524266, 'recovered_cases': 515385, 'recovered_rate': 62.78}]

print(type(obj[1]))
print(len(obj[1]))

print(obj[1])

