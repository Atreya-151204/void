# VOID // 001
### A Minimalist Serverless Web Application on AWS

VOID is a dark, minimalist web experience built to explore AWS serverless architecture, API integration, cloud permissions, and persistent data storage. It combines a lightweight HTML, CSS, and JavaScript frontend with a Python-based backend powered by AWS managed services.

The project demonstrates how a browser-based application can communicate with a serverless backend, process user input, and persist data without managing a traditional application server.

---

## Architecture

```text
                         USER
                          |
                          v
               +---------------------+
               |   VOID Frontend     |
               | HTML / CSS / JS     |
               +---------------------+
                          |
                          v
               +---------------------+
               |    AWS Amplify      |
               | Static Web Hosting  |
               +---------------------+
                          |
                          v
               +---------------------+
               |   Amazon API        |
               |   Gateway           |
               |   POST /void        |
               +---------------------+
                          |
                          v
               +---------------------+
               |    AWS Lambda       |
               |   Python Runtime    |
               +---------------------+
                          |
                 IAM-authorized access
                          |
                          v
               +---------------------+
               |   Amazon DynamoDB   |
               |   NoSQL Database    |
               +---------------------+
```

### Request lifecycle

1. A visitor opens the VOID website hosted through AWS Amplify.
2. The visitor submits a message through the minimalist input interface.
3. JavaScript sends an HTTP POST request to Amazon API Gateway.
4. API Gateway invokes the Python Lambda function.
5. Lambda processes the request, generates a unique ID and timestamp, and selects a response.
6. Lambda uses its IAM execution role to write the interaction to Amazon DynamoDB.
7. The browser performs a subtle fade, blur, and upward-drift animation, making the submitted text appear to dissolve into the interface.

The frontend animation runs independently of the backend response. This keeps the interaction visually simple while the serverless request is processed.

---

## AWS Services Used

### 1. AWS Amplify — Frontend Hosting

**Purpose:** Hosting and deploying the static website.

Amplify serves the HTML, CSS, and JavaScript that power the VOID interface.

What this demonstrates:
- Deploying a static website to AWS.
- Managing application hosting and deployment branches.
- Publishing frontend changes without operating a web server.
- Connecting a browser-based application to a cloud API.

### 2. Amazon API Gateway — HTTP API Layer

**Purpose:** Providing an HTTP endpoint for frontend-to-backend communication.

The project uses an API Gateway REST API with a `POST /void` resource.

What this demonstrates:
- Creating REST API resources and methods.
- Configuring Lambda integration.
- Passing JSON request bodies to backend code.
- Testing API requests and responses.
- Understanding cross-origin resource sharing (CORS) for browser requests.

### 3. AWS Lambda — Serverless Backend

**Purpose:** Executing application logic without managing a server.

The `void` function is written in Python. It accepts the submitted message, generates a unique identifier and UTC timestamp, chooses a response, and attempts to save the interaction to DynamoDB.

What this demonstrates:
- Event-driven serverless computing.
- Processing API Gateway events.
- Parsing JSON input and returning HTTP-style responses.
- Using the AWS SDK for Python (Boto3).
- Handling function execution and debugging through test results and logs.

### 4. AWS Identity and Access Management (IAM) — Permissions

**Purpose:** Controlling what the Lambda function is allowed to access.

The Lambda execution role grants the function permission to write items to the `voiddatabase` DynamoDB table.

The principle of least privilege means granting only the permissions needed for a task, ideally scoped to the specific table.

What this demonstrates:
- Understanding IAM roles and identity-based policies.
- Separating application code from cloud permissions.
- Authorizing service-to-service access without embedding AWS credentials in the website.
- Understanding why a function can execute successfully but still fail when its role lacks database permissions.

### 5. Amazon DynamoDB — Persistent Data Storage

**Purpose:** Storing submitted messages and their associated metadata.

The `voiddatabase` table uses `ID` as its string partition key.

Each saved interaction contains:

| Attribute | Purpose |
|---|---|
| `ID` | Unique identifier for the interaction |
| `Alias` | Name or alias supplied by the application |
| `UserMessage` | Submitted message |
| `Response` | Response generated by Lambda |
| `Timestamp` | UTC time associated with the interaction |

What this demonstrates:
- Creating and configuring a NoSQL database table.
- Choosing a partition key.
- Writing records from Lambda using Boto3.
- Inspecting persisted data to verify backend behavior.

---

## Technology Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, JavaScript |
| Hosting | AWS Amplify |
| API | Amazon API Gateway (REST API) |
| Backend | AWS Lambda, Python |
| AWS SDK | Boto3 |
| Database | Amazon DynamoDB |
| Access control | AWS IAM |
| Region | `eu-north-1` (Europe/Stockholm) |

---

## Interface and Interaction Design

VOID uses a restrained monochrome aesthetic with a black background, subtle typography, and randomly positioned ambient text fragments.

The input interaction is designed around disappearance rather than displaying a conventional confirmation message.

When a visitor submits a message:
- The text fades out.
- A slight blur accompanies the fade.
- The text drifts upward.
- The input clears after the animation.

The interaction is a frontend animation; it does not itself confirm whether the backend successfully stored the message. Backend success can be verified through the API response and DynamoDB records.

---

## Project Structure

```text
void/
├── index.html
├── README.md
├── backend/
│   └── lambda_function.py
├── docs/
│   └── architecture.md
└── screenshots/
    ├── 01-amplify-deployment.png
    ├── 02-api-gateway-lambda-integration.png
    ├── 03-lambda-success.png
    └── 04-dynamodb-records.png
```

- `index.html` — frontend interface and interaction logic.
- `backend/lambda_function.py` — Python Lambda handler.
- `docs/architecture.md` — additional architecture and request-flow notes.
- `screenshots/` — evidence captured during development and testing.

---

## Testing and Verification

During development, the individual components were tested through their AWS consoles.

- **Amplify:** The website branch showed a successful deployment.
- **API Gateway:** The `POST /void` method was configured with a Lambda integration.
- **Lambda:** A test execution succeeded and returned a response containing `"saved": true`.
- **DynamoDB:** Saved interaction records were visible in the table's Explore items view.

Together, these checks provide evidence that the backend integration worked during testing.

Screenshots are included in the repository as a development record.

---

## Security Considerations

This project was created as a learning prototype. Important considerations for a production deployment include:

- **IAM least privilege:** Restrict access to only the required resources and actions.
- **Input validation:** Validate and constrain user-supplied input on the backend.
- **CORS:** Configure allowed origins and methods appropriately.
- **Abuse prevention:** Add throttling, rate limits, and moderation before accepting public submissions.
- **Privacy:** Avoid collecting sensitive personal information and provide a suitable privacy notice.
- **Error handling:** Log useful diagnostic information without exposing internal errors to visitors.
- **Credentials:** Never place AWS secret access keys or other credentials in frontend code or GitHub.

The current prototype is not intended to be a production-ready anonymous messaging platform.

---

## Cost Awareness and Resource Lifecycle

The project was built using AWS managed services to learn how a small application can be assembled from separate cloud components.

The AWS resources used during development were subsequently removed to avoid ongoing usage and to keep the learning project cost-conscious.

The repository preserves the source code, architecture documentation, and screenshots. It does not preserve the live AWS infrastructure or automatically recreate it.

To restore the live backend, the AWS resources, permissions, integrations, and deployment configuration must be recreated.

---

## Key Learning Outcomes

Through VOID, I gained practical experience with:

- Deploying a static frontend using AWS Amplify.
- Building a REST endpoint with Amazon API Gateway.
- Connecting API Gateway to an AWS Lambda function.
- Writing Python backend logic using Boto3.
- Configuring IAM execution-role permissions for DynamoDB access.
- Persisting application data in Amazon DynamoDB.
- Testing serverless integrations and inspecting stored records.
- Understanding CORS, asynchronous browser requests, and frontend/backend boundaries.
- Documenting cloud architecture and maintaining evidence of implementation.

---

## Future Improvements

Potential next steps include:

- Reproducible infrastructure deployment using AWS SAM, AWS CDK, or Terraform.
- Automated tests for the Lambda handler and API integration.
- Improved validation, throttling, and monitoring.
- A clearer privacy and data-retention policy.
- A repeatable deployment pipeline from GitHub.
- A documented teardown procedure for cost control.

---

**Project status:** Learning prototype; AWS resources removed after development.

**Focus:** Serverless architecture, API integration, IAM permissions, NoSQL persistence, and minimalist interaction design.