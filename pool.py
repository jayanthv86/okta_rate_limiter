import os
import subprocess

companyUrl = input("Enter your Okta URL(company.okta.com) without https or www:")
apiKey = input("Enter the API key from the Okta tenant:")

template = 'python rate_limiter.py {0} {1}'.format(companyUrl, apiKey)

# Run commands in parallel
processes = []

for i in range(1,6):
    process = subprocess.Popen(template, shell=True)
    processes.append(process)

# Collect statuses
output = [p.wait() for p in processes]
