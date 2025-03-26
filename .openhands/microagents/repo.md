---
name: ai-gateway
type: repo
agent: CodeActAgent
---

Repository: AI Gateway
Description: A unified API for LLM inference, enabling efficient pair programming with agents. The repository leverages Not Diamond for model selection, Portkey for load balancing, and provides features like automatic retries, fallback mechanisms, prompt caching, and observability.

Directory Structure:
- apps/api: FastAPI endpoint for LLM inference
- apps/gateway: Cloudflare Workers for edge routing
- packages/ui: Shared UI components
- project-documentation: Documentation and architecture diagrams

Setup:
1. Install dependencies: `pnpm install`
2. Start the development server: `pnpm run dev`
3. Run tests: `pnpm test`

Development Guidelines:
- Use TypeScript for all new code.
- Follow ESLint and Prettier configurations.
- Write unit tests for all new features.
- Use FastAPI for the unified LLM inference endpoint.
- Avoid using npm; always use pnpm for package management.
- Transition Python dependency management from uv to pdm.

Testing Requirements:
- Unit tests must cover all new features.
- Integration tests for API endpoints.
- End-to-end tests for critical workflows.

Key Features:
1. **Model Selection**: Not Diamond selects the best model for each task based on continuous training and improvement.
2. **Load Balancing**: Portkey distributes requests across multiple providers to mitigate rate limiting and quota usage.
3. **Resilience**: Automatic retries and fallback mechanisms ensure reliability.
4. **Prompt Management**: Efficient prompt caching and management for optimized performance.
5. **Observability**: Comprehensive monitoring and logging for debugging and insights.

Workflow:
1. Send requests to the FastAPI endpoint.
2. Not Diamond selects the appropriate model for the task.
3. Portkey handles load balancing and provider selection.
4. Responses are returned with observability data for analysis.

Best Practices:
- Keep instructions updated as the project evolves.
- Document all dependencies and setup steps clearly.
- Include examples of good code patterns and conventions.
- Regularly review and update the microagent instructions to reflect changes in the repository.
