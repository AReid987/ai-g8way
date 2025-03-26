# AI Gateway

## Problems
- A host of common problems exist for LLM & Agentic Applications when deployed to production.
- Unaddressed, these problems diminish the benefits and usefulness of AI applications.
## Soluction
- AI Gateway
- A 4 part systems composed of:
    -  A FastAPI providing a Singular Endpoint which enables access to all accessible LLM Inference Providers
- An LLM serving as an Intelligent Model Router, selecting the best model for a given task and continuously improving in real time
- An LLM Control panel providing a Suite of features:
    - Solutions for common problems
    - Robust LLM Observability
    - Debugging Tools
- Evaluations Tools
    - Several Tools for various aspects of Evaluation & Experiments
    - Fine Grained Development of a system to the use case rather than guess and check
    - Mitigating the Black Box
## Functionality
### Outperform Every Singular Foundation Model
- Large & Small Model pairs outperform on every major benchmark
#### Predictive Model Recommendation per Input
- Each task receives an optimal model recommendations at every particular step
- Feedback given at any point in time is used by the Selector Model for self improvement
#### RoRF - Routing on Random Forests
- Strong & Weak Model pairs reduce cost & latency while maintaining performance
### Cost & Latency Reduction
#### Leverage Smaller, Cheaper Model with no performance loss
- Configure Custom Model for desired outcome, e.g., favor cost or latency optimization
### RAG Auto Eval and Optimization
#### Generate Test Data, Eval & Optimize
- Use document store to generate test data
- Evaluate various LLMs on a RAG Pipeline
### Observability
#### Logs
- Track many metrics at various levels of Granularity
#### Tracing
- Monitor Lifecycle of LLM Requests in chronological view
#### Analytics
- Track various metrics related to requests to different LLMS
- Costs, Latencies, Tokens, User Activity, Feedback, Cache Hits, Errors, etc
- Observe efficiency, areas for optimization, discover patterns, etcf
#### Metadata Enrichment
- Enrich requests with metadata for later filtering or auditing
#### Feedback
- Weighted Customer Feedback on any request at any stage
#### Budget Limits for Provider API Keys
- Manage & Limit spending by Provider / LLM
### Unified AI API
#### Universal API Endpoint
- Consistent Interface for all modalities and LLM Providers
#### Prompt Caching
- Optimize cost by storing past responses for reuse on similar queries
#### Fallbacks
- Enhance reliability
- Fallback to model or list of models based on conditions, e.g., Status Code, response outcome, etc.
#### Conditional Routing
- Route to models based on conditions, e.g., user location, user account tier, etc.
#### Multimodality
- One interface for Chat, Text, Embeddings, Vision, Image Generation, Audio, Video, and across providers
#### Automatic Retries
- Configurable, retry up to 5 times for the frequent, inexplicable failures.
- Configure e.g., based on status code
- Exponential Backoff
#### Load Balancing
- Distribute requests across multiple Providers for balanced quota usage
- Configurable
#### Canary Testing
- Configurable
- Introduce new models or prompts in specific amounts and / or environments
#### Virtual API Keys
- Streamline API Key Management, Rotation, enhancing security
#### Request Timeouts
- Terminate requests reaching timeout and send a faster, or more reliable request to a different provider
#### Budget Limiting
- One time or monthly limit to stop usage beyond the desired limit
#### Rate Limiting
- Programmatically set limits at API Key level
### Prompt Library
- Create and manage prompts along with Model Parameters
- Prompt versioning
#### Prompt templates
- Variables in prompts for dynamic, reusable templates
#### Prompt Partials
- Store commonly used templates separately for use within Prompt Templates
### Guardrails
#### PII Redaction
- Replace sensitive data with standard Identifiers
#### Toxicity & Prompt Injection Guard
- Scan Prompts and Responses
#### Hallucination Guard
- afterRequestHook 
#### Conciseness & Helpfulness Checks
#### Gender & Racial Bias Checks
- afterRequestHook 
#### Model Manipulation, Malicious Content & Data Transfer Guard
- Analyze & Redact Texts for safeguarding
### Autonomous Fine Tuning
#### Continuous Learning & Performance Enhancement
- Automate workflows from Data Prep to model deployment
- Multi provider
- Data Informed Continuous Improvement
- Schedule to Keep Module Up to Date
#### Data Prep, Enrichment & Creation
- Collect logs
- Automated Log Annotation
- Leverage Filters to select most relevant logs for dataset creation
- Export Enriched logs as dataset
- Select LLM 
- Configure Fine Tuning Parameters
- Kickoff job & Monitoring
- Deploy Model
- Schedule Periodic Fine tuning jobs




