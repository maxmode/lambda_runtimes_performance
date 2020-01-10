# Which Lambda runtime is faster? 

Node, Python, Go, Ruby, Java or .Net?

Which Lambda runtime is more performance consistent?

Which Lambda runtime has lower cold starts / freeze startup?

# Execution

To test lambda performance - I've implemented a simple Lambda application 
on all the runtimes (Golang, Python, Node, Java, Ruby, .Net).

All Lambda functions are connected to API Gateway and can be tested as REST API.

For runtimes Node, Python and Ruby - source code was copied from AWS Console sample functions.
For Java, Go and .Net - source code was written from scratch.
All implementations (on all languages) act the same - they just reply with text "Hello from Lambda!"

As a testing tool - was chosen Locust. Tth test file is located in ```locustfile.py```

The test was executed on AWS CodeBuild for 5 minutes. For the full results see section "Full results" below.

![Test setup diagram](setup_diagram.png?raw=true "Title")

This test will check how fast AWS can spin up Lambda functions in different runtimes.

For cold starts - be aware that it depends on the Lambda package size.
Package size for of this sample application:
- Node.js, Python, Ruby, Golang - 7.7Mb
- Java - 1Mb
- .Net - 82Kb

# Conclusion

In terms of performance **Go (Golang) runtime appeared to be the fastest**. 
Golang is 24% faster than average in this test. 
Also Golang appeared to be the most stable, with minimum cold starts.

The silver medal for performance took Python, and bronze - goes to Node.js**.

| Runtime  | Performance (top 80%) | Cold starts (top 99,9%) |  . |
|----------|--------- |--------------|-----------------------------------------|
| 🥇 Golang   | 52ms 🥇  |  170ms 🥇    | Golang - best performance and stability |
| 🥈 Python   | 68ms 🥈  |  190ms       | Python - golden middle |
| 🥉 Node.js  | 75ms 🥉  |  190ms       | Node.js - performance competing with Python |
| .Net     | 52ms 🥇  |  730ms 💩💩💩| .Net - very fast but too many cold starts
| Java     | 65ms     |  510ms 💩💩  | Java - many cold starts
| Ruby     | 79ms 💩  |  210ms       | Ruby - the slowest |

.Net has too many cold starts, despite being same fast as Golang.
Java also have a lot of cold starts.
And least performing appeared to be the Ruby runtime.

Based on this, Golang is the fastest Lambda runtime nowadays, followed by Node and Python, which are also OK.
While Java, .Net, and Ruby are either slow either have an unpredictable cold starts, 
so better stay away from these languages within Lambda environment.

# Full results
```
Name       # reqs      # fails     Avg     Min     Max  |  Median   req/s failures/s
------------------------------------------------------------------------------------
 dotnet2.1   9692     0(0.00%)      55      43    4184  |      48   32.19    0.00
 golang      9694     0(0.00%)      53      43     248  |      48   32.20    0.00
 java11      9694     0(0.00%)      58      43    1015  |      49   32.20    0.00
 node12      9697     0(0.00%)      56      43     340  |      49   32.21    0.00
 python3.8   9697     0(0.00%)      59      44     301  |      52   32.21    0.00
 ruby2.5     9694     0(0.00%)      67      45     357  |      63   32.20    0.00
------------------------------------------------------------------------------------
 Aggregated 58168     0(0.00%)      58      43    4184  |      50  193.21    0.00

Percentage of the requests completed within given times
 Name      # reqs    50%    66%    75%    80%    90%    95%    98%    99%  99.9% 99.99%   100%
----------------------------------------------------------------------------------------------
 dotnet2.1   9692     48     49     51     52     78     81     86    100    730   4200   4200
 golang      9694     48     49     50     52     78     80     84     92    170    250    250
 java11      9694     49     51     56     65     81     89    120    150    510   1000   1000
 node12      9697     49     51     54     75     80     83     95    110    190    340    340
 python3.8   9697     52     59     63     68     82     88     97    110    190    300    300
 ruby2.5     9694     63     68     75     79     91     98    110    120    210    360    360
----------------------------------------------------------------------------------------------
Aggregated  58168     50     55     62     68     81     87    100    120    220   1400   4200
```

# Reproduce test yourself

### Preconditions

1. You should have AWS account and AWS CLI configured
1. Serverless is installed

### Steps

1. Checkout this repository
2. Run ```sls deploy```
3. Go to AWS console -> Code Build (region Ireland)
4. Create a new CodeBuild job.
    - As a source - specify this repository
    - Buildspec - specify buildspec.yml from the repository
    - Environment variables: 
   - BASE_URL = {common url of your deployed APIs, should be in output on "sls deploy" command}
5. Run the job    

**Test results will be in the job's output.**
