# VOID architecture notes

## Request flow

1. A visitor enters a message in `index.html`.
2. The browser starts a `POST` request to API Gateway at `/dev/void`.
3. API Gateway invokes the Python Lambda function named `void`.
4. Lambda creates an ID and timestamp, chooses a demo response, and writes the interaction to DynamoDB table `voiddatabase`.
5. The browser-side input animation is independent of the API response and clears after approximately 850 ms.

## DynamoDB item attributes

- `ID` — unique UUID string and partition key.
- `Alias` — visitor alias (the website currently sends `Visitor`).
- `UserMessage` — submitted text.
- `Response` — random response returned by Lambda.
- `Timestamp` — UTC timestamp.

## Evidence checklist

- Amplify app/branch deployment.
- API Gateway `POST /void` method and Lambda integration.
- Lambda successful test response with `saved: true`.
- DynamoDB item showing the submitted message.
- Deployed website showing the UI.
