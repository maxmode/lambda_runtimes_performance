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

## Performance
In terms of performance **Go (Golang) runtime appeared to be the fastest**. Golang is 11% faster than average in this test.
**The second place for performance took Node.js**. Node is 7% faster than average.

| Runtime    | Average performance | Fastest run, ms |
|------------|---------|----------|
| 🥇Golang   | 54ms    |     43ms |
| 🥈Node.js  | 57ms    |     44ms |
| 😐Python   | 60ms    |     45ms |
| 😐Java     | 63ms    |     45ms |
| 💩.Net     | 65ms    |     44ms |    
| 💩Ruby     | 68ms    |     46ms |

Least performing in our test appeared to be Ruby and .Net runtimes.

## Cold Starts
In terms of stability and minimum cold starts - clear winner is Golang 1.x runtime, 
the maximum cold start for it was less than 280ms, 
The second place is shared between Node 12.x, Python 3.8 and Ruby2.5 
with a maximum cold start around 400ms.

| Runtime    | Maximum cold start, ms |
|------------|---------|
| 🥇Golang   | 280ms    |
| 🥈Ruby     | 400ms    |
| 🥈Node.js  | 410ms    |
| 🥈Python   | 460ms    |
| 💩Java     | 1100ms   |
| 💩.Net     | 4900ms   | 

The least stable appeared to be .Net (dotnetcore2.1, cold start 4948ms) and Java (java11, cold start 1097ms)

Based on this, Golang is the fastest Lambda runtime nowadays, followed by Node and Python, which are also OK.
While Java, .Net, and Ruby are either slow either have an unpredictable cold starts, 
so better stay away from these languages within Lambda environment.

# Full results
```
Name               # reqs   # fails      Avg     Min     Max  |  Median   req/s  failures/s
---------------------------------------------------------------------------------------------------
 GET dotnet2.1     3214     0(0.00%)      65      44    4948  |      48   10.68    0.00
 GET golang        3214     0(0.00%)      54      43     276  |      48   10.68    0.00
 GET java11        3214     0(0.00%)      63      45    1097  |      50   10.68    0.00
 GET node12        3220     0(0.00%)      57      44     412  |      49   10.70    0.00
 GET python3.8     3219     0(0.00%)      60      45     456  |      53   10.69    0.00
 GET ruby2.5       3215     0(0.00%)      68      46     400  |      63   10.68    0.00
---------------------------------------------------------------------------------------------------
 Aggregated       19296     0(0.00%)      61      43    4948  |      50   64.11    0.00

Percentage of the requests completed within given times
 Type Name           # reqs    50%    66%    75%    80%    90%    95%    98%    99%  99.9% 99.99%   100%
--------------------------------------------------------------------------------------------------------
 GET  dotnet2.1       3214     48     49     51     52     78     81     86    100   4900   4900   4900
 GET  golang          3214     48     49     51     53     78     81     85    100    260    280    280
 GET  java11          3214     50     55     63     73     83    100    150    180    960   1100   1100
 GET  node12          3220     49     51     55     77     81     83     95    130    360    410    410
 GET  python3.8       3219     53     60     64     69     83     91     98    110    330    460    460
 GET  ruby2.5         3215     63     68     76     81     91     99    110    120    340    400    400
--------------------------------------------------------------------------------------------------------
 None Aggregated     19296     50     56     64     71     81     89    110    140    460   4900   4900
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
