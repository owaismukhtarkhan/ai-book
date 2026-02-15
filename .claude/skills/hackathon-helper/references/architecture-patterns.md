# Project Architecture Patterns

## Core Principles

### Global Guiding Principles
1. **Clarity First**: All documentation must be clear, concise, and actionable
2. **Modularity**: Break complex projects into manageable, independent phases
3. **Progressive Disclosure**: Present information in layers, from high-level to detailed
4. **Consistency**: Maintain uniform structure and naming conventions across all files
5. **Traceability**: Ensure every decision and requirement can be traced back to source

### Technical Standards
1. **File Organization**: Use clear, logical directory structures
2. **Naming Conventions**: Follow consistent, descriptive naming patterns
3. **Documentation Quality**: All generated files must be complete and well-structured
4. **Version Control**: Maintain clear commit history and change tracking

## Phase Structure Patterns

### Phase Identification
Each phase should have:
- **Clear Objective**: What this phase accomplishes
- **Deliverables**: Specific outputs or artifacts
- **Dependencies**: What must be completed before starting
- **Success Criteria**: How to measure completion

### Specification File Structure
```markdown
# Phase Title

## Overview
Brief description of the phase and its purpose

## Objectives
- Specific goals to achieve
- Success criteria

## Deliverables
- List of expected outputs
- Format and quality standards

## Prerequisites
- Required knowledge or resources
- Dependencies on other phases

## Process
Step-by-step instructions for completing the phase

## Validation
How to verify the phase is complete
- Tests or checks
- Acceptance criteria
```

## Global File Templates

### constitution.md Template
```markdown
# Project Constitution

## Vision and Mission

## Core Values

## Guiding Principles

## Rules of Engagement

## Decision Making Framework

## Success Metrics
```

### claude.md Template
```markdown
# Claude Code Guidelines

## Technical Instructions

## Coding Standards

## Persona Guidelines

## Quality Standards

## Review Process

## Communication Guidelines
```

## Roadmap Structure

### steps.md Template
```markdown
# Project Implementation Steps

## Phase 1: [Phase Name]
- [ ] Step 1: [Description]
- [ ] Step 2: [Description]
- [ ] Step 3: [Description]

## Phase 2: [Phase Name]
- [ ] Step 1: [Description]
- [ ] Step 2: [Description]
- [ ] Step 3: [Description]

## Phase 3: [Phase Name]
- [ ] Step 1: [Description]
- [ ] Step 2: [Description]
- [ ] Step 3: [Description]
```

## Quality Assurance

### File Completeness Checklist
- [ ] All required sections are present
- [ ] Content is coherent and well-organized
- [ ] Naming conventions are followed
- [ ] Dependencies and prerequisites are clear
- [ ] Success criteria are measurable

### Consistency Guidelines
- Use consistent terminology across all files
- Maintain parallel structure in similar sections
- Follow the same formatting patterns
- Ensure logical flow between phases