 # Claude AI Assistant Guidelines for NetDocGen

## Overview
This document outlines how Claude AI can assist with the NetDocGen (Network Documentation Generator) project development, troubleshooting, and enhancement.
Always refer to the TASKS.md file for the current development tasks and mark it complete when completed. Always ensure that there are no bugs or issues after completing each task.
DO NOT USE SIMPLIFY OR SIMPLE SCRIPT EVER! This will break the project. DO NOT USE EMOJIS. This will break the project.
TEMPORARY: Skip the Security Hardening section (SEC-001 through SEC-005) in Phase 6 for now.

## Important: LLM Usage Policy
The LLM (Phi model via Ollama) is used ONLY for enhancing documentation quality. It does NOT provide network design recommendations.

The LLM assists with:
- Writing professional executive summaries
- Generating technical glossaries
- Enhancing device descriptions for clarity
- Explaining connection types
- Suggesting documentation structure and organization

The LLM does NOT:
- Provide network design recommendations
- Suggest security improvements to the network
- Recommend network optimizations
- Analyze network vulnerabilities

This ensures the tool remains focused on documentation quality rather than network consulting.
## Key Assistance Areas

### 1. Code Development
- **Visio Parser Enhancement**: Help implement complex XML parsing logic for various Visio diagram formats
- **Template Development**: Assist in creating Jinja2 templates for different documentation sections
- **API Design**: Review and suggest improvements for RESTful API endpoints
- **Error Handling**: Implement comprehensive error handling patterns

### 2. Architecture Decisions
- Review microservices communication patterns
- Suggest optimal data flow between services
- Recommend caching strategies
- Propose security best practices

### 3. Documentation Generation
- Help create dynamic content generation algorithms
- Assist with network topology analysis logic
- Develop intelligent content organization strategies
- Implement cross-referencing systems

### 4. Testing Strategies
- Unit test generation for critical components
- Integration test scenarios
- Performance test planning
- Security testing recommendations

## Prompt Examples

### For Code Review
```
"Review this Visio parser implementation and suggest improvements for handling complex network diagrams with nested shapes and custom properties."
```

### For Architecture
```
"Analyze the microservices architecture for NetDocGen and recommend improvements for handling concurrent document generation requests at scale."
```

### For Problem Solving
```
"The Visio parser is failing to extract VLAN information from certain diagram formats. Here's the error log and sample XML. How can we fix this?"
```

## Best Practices for Interaction

1. **Provide Context**: Always include relevant code snippets, error messages, and expected behavior
2. **Be Specific**: Focus on one component or issue at a time
3. **Include Examples**: Provide sample data or test cases when applicable
4. **Iterate**: Use follow-up questions to refine solutions

## Limitations to Consider

- Claude doesn't have direct access to your codebase or runtime environment
- Visual diagram interpretation requires structured data (XML/JSON)
- Real-time debugging requires detailed error logs and context
- Third-party library specifics may need documentation references

## Integration Points

### Development Workflow
1. Use Claude for initial design discussions
2. Get code review suggestions before PR
3. Troubleshoot complex parsing scenarios
4. Generate test cases and documentation

### Continuous Improvement
- Regular architecture reviews
- Performance optimization suggestions
- Security audit assistance
- Feature ideation and planning