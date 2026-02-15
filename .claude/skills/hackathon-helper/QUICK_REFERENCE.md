# Hackathon Helper Quick Reference Guide

## Core Operations

### Project Analysis
```bash
# Analyze provided .md file
analyze_project(
    file_path: str,
    output_format: str = "detailed"
) -> AnalysisReport
```

**Key Steps:**
1. Read and validate input file
2. Extract project requirements
3. Identify phases and deliverables
4. Validate technical specifications
5. Generate analysis summary

### Documentation Generation
```bash
# Generate complete project structure
generate_documentation(
    project_name: str,
    analysis_data: dict,
    output_path: str = "."
) -> ProjectStructure
```

**Files Generated:**
- `constitution.md` - Project constitution
- `claude.md` - Claude integration guide
- `spec-*.md` - Phase specifications
- `guide-*.md` - Implementation guides
- `README.md` - Project overview

## Command Reference

### Analysis Commands
```bash
# Basic analysis
hackathon-helper analyze <file.md>

# Detailed analysis with technical validation
hackathon-helper analyze --detailed --validate-tech <file.md>

# Quick analysis for scoping
hackathon-helper analyze --quick <file.md>
```

### Generation Commands
```bash
# Generate complete project structure
hackathon-helper generate <project-name> <file.md>

# Generate specific components
hackathon-helper generate constitution <project-name>
hackathon-helper generate specs <project-name>
hackathon-helper generate guides <project-name>

# Dry run (preview without creating files)
hackathon-helper generate --dry-run <project-name> <file.md>
```

### Validation Commands
```bash
# Validate generated documentation
hackathon-helper validate <project-name>

# Check documentation standards
hackathon-helper validate --standards <project-name>

# Run comprehensive quality checks
hackathon-helper validate --comprehensive <project-name>
```

## Error Handling Quick Reference

### Common Issues

| Issue | Solution | Command |
|-------|----------|---------|
| Permission Denied | Check permissions, use sudo | `ls -la`, `chmod` |
| Disk Full | Clear temp files, use external storage | `df -h`, `rm -rf` |
| Network Timeout | Check connection, retry with backoff | `ping`, `curl` |
| Template Error | Validate syntax, check placeholders | `template validate` |

### Emergency Recovery
```bash
# System failure recovery
check_system_logs()
verify_disk_integrity()
restore_from_backup()

# Data corruption recovery
check_file_integrity()
attempt_data_recovery()
restore_from_version_control()
```

## Feedback Collection

### User Interaction Points
```markdown
1. **Initial Analysis:**
   - Project scope clarification
   - Technical requirement validation
   - Timeline feasibility assessment

2. **Documentation Generation:**
   - Content approval
   - Formatting preferences
   - Customization requests

3. **Final Review:**
   - Comprehensive feedback
   - Improvement suggestions
   - User satisfaction validation
```

### Feedback Commands
```bash
# Collect user feedback
hackathon-helper feedback collect <project-name>

# Analyze feedback patterns
hackathon-helper feedback analyze <project-name>

# Implement feedback changes
hackathon-helper feedback implement <project-name>
```

## Monitoring and Metrics

### Performance Metrics
```bash
# Track operation performance
hackathon-helper monitor performance

# Monitor resource usage
hackathon-helper monitor resources

# Track error rates
hackathon-helper monitor errors
```

### Quality Metrics
```bash
# Track documentation quality
hackathon-helper monitor quality <project-name>

# Monitor user satisfaction
hackathon-helper monitor satisfaction <project-name>

# Track completion rates
hackathon-helper monitor completion <project-name>
```

## Integration Points

### MCP Server Integration
```bash
# List available MCP servers
hackathon-helper mcp list

# Connect to MCP servers
hackathon-helper mcp connect <server-name>

# Configure MCP connections
hackathon-helper mcp configure <server-name>
```

### External Tool Integration
```bash
# Integrate with development tools
hackathon-helper integrate dev-tools <project-name>

# Configure testing tools
hackathon-helper integrate testing <project-name>

# Set up deployment tools
hackathon-helper integrate deployment <project-name>
```

## Quick Start Examples

### Basic Usage
```bash
# Analyze and generate complete project
hackathon-helper analyze hackathon-project.md
hackathon-helper generate hackathon-project hackathon-project.md

# Validate generated documentation
hackathon-helper validate hackathon-project
```

### Advanced Usage
```bash
# Analyze with technical validation
hackathon-helper analyze --detailed --validate-tech hackathon-project.md

# Generate with custom output path
hackathon-helper generate --output /projects/hackathon-project hackathon-project hackathon-project.md

# Run comprehensive validation
hackathon-helper validate --comprehensive hackathon-project
```

## Troubleshooting

### Common Problems

**1. File Creation Fails**
- Check directory permissions
- Verify disk space availability
- Use absolute paths
- Try alternative location

**2. Template Rendering Errors**
- Validate template syntax
- Check for missing placeholders
- Verify data structure
- Use fallback templates

**3. Network Integration Issues**
- Check network connectivity
- Verify API credentials
- Implement retry logic
- Use offline alternatives

**4. Performance Issues**
- Monitor resource usage
- Implement caching
- Optimize file operations
- Use efficient algorithms

### Recovery Procedures

**1. System Failure**
```bash
check_system_logs()
verify_disk_integrity()
restore_from_backup()
escalate_to_admin()
```

**2. Data Corruption**
```bash
check_file_integrity()
attempt_data_recovery()
restore_from_version_control()
document_data_loss()
```

**3. Security Breach**
```bash
isolate_affected_systems()
change_all_credentials()
review_access_logs()
conduct_security_audit()
notify_stakeholders()
```

## Best Practices

### Development Workflow
1. **Analyze First:** Always analyze requirements before generation
2. **Validate Early:** Validate inputs before processing
3. **Test Incrementally:** Test each phase separately
4. **Document Changes:** Keep track of all modifications

### Error Handling
1. **Graceful Degradation:** Provide alternatives when features fail
2. **User Feedback:** Always inform users of issues and resolutions
3. **Recovery Options:** Offer multiple recovery paths
4. **Logging:** Maintain detailed logs for troubleshooting

### Quality Assurance
1. **Standards Compliance:** Follow established documentation standards
2. **User Validation:** Validate outputs with users
3. **Continuous Improvement:** Regularly update based on feedback
4. **Performance Monitoring:** Track and optimize performance

This quick reference guide provides essential commands, procedures, and best practices for effective use of the Hackathon Helper skill. Keep this guide accessible for rapid reference during project execution.