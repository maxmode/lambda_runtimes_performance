package main

import (
    "github.com/aws/aws-lambda-go/lambda"
)

type response struct {
    Body string `json:"body"`
    StatusCode string `json:"statusCode"`
}

func show() (*response, error) {
    r := &response{
        Body: "Hello from Lambda!",
        StatusCode: "200",
    }

    return r, nil
}

func main() {
    lambda.Start(show)
}